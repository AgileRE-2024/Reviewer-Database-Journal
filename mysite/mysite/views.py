from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import requests
from myapp.models import ScrapedPaper, Reviewer, DetailReviewer

def scrape_reviewers(request):
    file_path = "C:\\Users\\Kevin\\Downloads\\USERS JISEBI.xlsx"
    try:
        # Membaca kolom givenname, affiliation, country, email, orcid, dan username dari file Excel
        df = pd.read_excel(file_path)
        reviewer_data = df[['givenname.Element:Text', 'affiliation.Element:Text', 'country', 'email', 'orcid', 'username']].fillna('NULL')

        headers = {'User-Agent': 'Postman'}

        for _, row in reviewer_data.iterrows():
            name = row['givenname.Element:Text']
            affiliation = row['affiliation.Element:Text']
            country = row['country']
            email = row['email']
            orcid = row['orcid']
            username = row['username']

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

                        # Menyimpan semua penulis dalam format string
                        authors_list = [f"{author.get('given', '')} {author.get('family', '')}".strip() for author in authors]
                        authors_str = ", ".join(authors_list)

                        abstract = item.get('abstract', 'No Abstract')

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

        return JsonResponse({'message': 'Scraping completed and data saved to the database'})

    except Exception as e:
        print(f"Error occurred: {e}")
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