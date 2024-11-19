from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import pandas as pd
import requests
from myapp.models import ScrapedPaper, Reviewer, DetailReviewer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from django.views.decorators.csrf import csrf_exempt 
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

def get_statistics(request):
    total_papers = ScrapedPaper.objects.count()
    total_reviewers = Reviewer.objects.count()
    return JsonResponse({
        'total_papers': total_papers,
        'total_reviewers': total_reviewers,
    })

@csrf_exempt
def recommend_reviewers(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        input_title = data.get('title', '')
        input_abstract = data.get('abstract', '')

        # Menggabungkan input title dan abstract untuk pencocokan
        user_input = f"{input_title} {input_abstract}"

        # Ambil semua paper dari database untuk dibandingkan
        papers = ScrapedPaper.objects.all()
        paper_texts = [f"{paper.title} {paper.abstract}" for paper in papers]

        # Tambahkan input user ke daftar teks untuk dihitung similiaritasnya
        paper_texts.insert(0, user_input)

        # Hitung TF-IDF dan Cosine Similarity
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(paper_texts)
        cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix).flatten()

        # Mengambil semua hasil kemiripan dengan filter nilai similarity > 10%
        similar_papers = [
            (papers[i-1], cosine_similarities[i] * 100)  # i-1 karena indeks 0 adalah input user, konversi ke persentase
            for i in range(1, len(cosine_similarities))
            if cosine_similarities[i] * 100 > 10  # Filter nilai similarity > 10%
        ]

        # Mengelompokkan reviewer dan menyimpan nilai similarity tertinggi
        reviewer_dict = {}
        for paper, score in similar_papers:
            reviewer = paper.reviewer
            if reviewer.name not in reviewer_dict:
                reviewer_dict[reviewer.name] = {
                    'highest_score': score,  # Nilai similarity tertinggi
                    'count': 0,  # Tambahkan penghitung jumlah paper
                    'papers': [],
                    'email': reviewer.detail.email,
                    'country': reviewer.detail.country
                }
            else:
                # Perbarui nilai similarity tertinggi jika ditemukan skor lebih tinggi
                reviewer_dict[reviewer.name]['highest_score'] = max(reviewer_dict[reviewer.name]['highest_score'], score)

            # Tambahkan paper ke daftar
            reviewer_dict[reviewer.name]['count'] += 1  # Tambahkan ke penghitung
            reviewer_dict[reviewer.name]['papers'].append({
                'title': paper.title,
                'similarity_score': round(score, 2),
                'url': paper.url
            })

        # Sort reviewer berdasarkan nilai similarity tertinggi
        top_reviewers = sorted(
            reviewer_dict.items(),
            key=lambda item: item[1]['highest_score'],
            reverse=True
        )[:10]

        # Format data untuk dikirim ke frontend, urutkan papers berdasarkan similarity score
        recommendations = [
            {
                'name': name,
                'highest_score': round(data['highest_score'], 2),
                'count': data['count'],  # Tambahkan count ke data
                'papers': sorted(data['papers'], key=lambda x: x['similarity_score'], reverse=True)
            }
            for name, data in top_reviewers
        ]

        return JsonResponse(recommendations, safe=False)


    
@csrf_exempt
def get_reviewer_details(request):
    if request.method == 'GET':
        reviewer_name = request.GET.get('name')
        # Ambil reviewer berdasarkan nama (pastikan unik)
        reviewer = get_object_or_404(Reviewer, name=reviewer_name)
        detail = reviewer.detail  # OneToOneField relationship ke DetailReviewer

        # Format data untuk dikirimkan ke frontend
        detail_data = {
            'name': reviewer.name,
            'email': detail.email,
            'country': detail.country,
            'orcid': detail.orcid,
            'username': detail.username,
        }
        return JsonResponse(detail_data)
    
def upload_ojs_file(request):
    if request.method == 'POST' and request.FILES.get('ojs_file'):
        ojs_file = request.FILES['ojs_file']
        file_path = default_storage.save(f"uploads/{ojs_file.name}", ContentFile(ojs_file.read()))
        request.session['ojs_file_path'] = file_path  # Simpan path file di sesi untuk digunakan nanti
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def scrape_reviewers(request):
    file_path = request.session.get('ojs_file_path')
    if not file_path:
        return JsonResponse({'error': 'No file uploaded'})

    try:
        # Baca file Excel dari path yang disimpan di sesi
        df = pd.read_excel(default_storage.open(file_path))
        # Daftar kolom yang diharapkan
        required_columns = ['givenname', 'familyname', 'affiliation.Element:Text', 'country', 'email', 'orcid', 'username']

        # Cek apakah kolom yang diharapkan ada di file Excel
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            return JsonResponse({'error': f"Kolom pada Excel tidak sesuai dengan format. Kolom yang hilang: {', '.join(missing_columns)}"})

        # Jika semua kolom ada, lanjutkan proses scraping
        reviewer_data = df[required_columns].fillna('NULL')

        headers = {'User-Agent': 'Postman'}

        for _, row in reviewer_data.iterrows():
            givenname = row['givenname']
            familyname = row['familyname']
            affiliation = row['affiliation.Element:Text']
            country = row['country']
            email = row['email']
            orcid = row['orcid']
            username = row['username']

            # Kombinasikan givenname dan familyname untuk query
            name = f"{givenname} {familyname}"

            try:
                # Mengirim request ke CrossRef API dengan timeout 10 detik
                response = requests.get(
                    f"https://api.crossref.org/works?query.author={name}&query.affiliation={affiliation}",
                    headers=headers,
                    timeout=10
                )

                if response.status_code == 200:
                    data = response.json()
                    items = data.get('message', {}).get('items', [])

                    # Membuat atau mengambil reviewer
                    reviewer, _ = Reviewer.objects.get_or_create(name=name)
                    
                    # Menambahkan atau memperbarui DetailReviewer
                    DetailReviewer.objects.update_or_create(
                        reviewer=reviewer,
                        defaults={
                            'country': country,
                            'email': email,
                            'orcid': orcid,
                            'username': username
                        }
                    )

                    for item in items:
                        title = item.get('title', ['No Title'])[0]
                        url = item.get('URL', 'No URL')
                        authors = item.get('author', [])
                        publisher = item.get('publisher', 'No Publisher')

                        # Membuat daftar nama author dalam format string
                        authors_list = [f"{author.get('given', '')} {author.get('family', '')}".strip() for author in authors]
                        authors_str = ", ".join(authors_list)

                        abstract = item.get('abstract', 'No Abstract')

                        # Cek apakah salah satu author cocok dengan nama reviewer dari data OJS
                        match_found = any(
                            givenname.lower() in author.get('given', '').lower() and
                            familyname.lower() in author.get('family', '').lower()
                            for author in authors
                        )

                        if match_found:
                            # Cek apakah entri sudah ada berdasarkan judul atau URL
                            paper, created = ScrapedPaper.objects.get_or_create(
                                title=title,
                                url=url,
                                authors=authors_str,  # Menggunakan authors_str
                                abstract=abstract,
                                publisher=publisher,  # Menambahkan publisher
                                reviewer=reviewer
                            )

                            if created:
                                print(f"Title: {title}")
                                print(f"URL: {url}")
                                print(f"Authors: {authors_str}")
                                print(f"Publisher: {publisher}")

                else:
                    print(f"Failed to fetch data for {name} (status code: {response.status_code})")

            except requests.exceptions.RequestException as req_err:
                print(f"Request error for {name}: {req_err}")

        return JsonResponse({'message': 'Scraping completed and data saved to the database if match found'})

    except Exception as e:
        return JsonResponse({'error': str(e)})

def DashboardPage(request):
    return render(request, 'dashboard.html')  

def FavoritePage(request):
    return render(request, 'favorite.html')  

def HistoryPage(request):
    return render(request, 'history.html')

def LoginPage(request):
    return render(request, 'login.html')

def SignupPage(request):
    return render(request, 'signup.html')

def UploadPaperPage(request):
    return render(request, 'upload-paper.html')

def UploadDetailPage(request):
    return render(request, 'upload-detail.html')

def ConfirmationPage(request):
    return render(request, 'confirmation.html')

def ReviewerPage(request):
    return render(request, 'reviewer.html')

def UploadOJSPage(request):
    return render(request, 'upload-ojs.html')

def ContactPage(request):
    return render(request, 'contact.html')

def RecommendationPage(request):
    return render(request, 'recommended-reviewers.html')