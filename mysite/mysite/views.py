from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import requests
from myapp.models import ScrapedPaper, Reviewer

def scrape_reviewers(request):
    file_path = "C:\\Users\\Kevin\\Downloads\\USERS JISEBI.xlsx"
    try:
        # Membaca kolom givenname dan affiliation dari file Excel
        df = pd.read_excel(file_path)
        reviewer_data = df[['givenname.Element:Text', 'affiliation.Element:Text']].dropna()

        headers = {'User-Agent': 'Postman'}

        for _, row in reviewer_data.iterrows():
            name = row['givenname.Element:Text']
            affiliation = row['affiliation.Element:Text']
            
            response = requests.get(
                f"https://api.crossref.org/works?query.author={name}&query.affiliation={affiliation}",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                items = data.get('message', {}).get('items', [])
                
                reviewer, _ = Reviewer.objects.get_or_create(name=name)  # Buat atau ambil reviewer

                for item in items:
                    title = item.get('title', ['No Title'])[0]
                    url = item.get('URL', 'No URL')
                    authors = item.get('author', [])
                    abstract = item.get('abstract', 'No Abstract')

                    first_author = ""
                    if authors:
                        first_author_data = authors[0]
                        first_author = f"{first_author_data.get('given', '')} {first_author_data.get('family', '')}".strip()
                    
                    # Cek apakah entri sudah ada berdasarkan judul atau URL
                    paper, created = ScrapedPaper.objects.get_or_create(
                        title=title,
                        url=url,
                        first_author=first_author,
                        abstract=abstract,
                        reviewer=reviewer  # Hubungkan paper ke reviewer
                    )

                    if created:
                        print(f"Title: {title}")
                        print(f"URL: {url}")
                        print(f"First Author: {first_author}")

            else:
                print(f"Failed to fetch data for {name} (status code: {response.status_code})")

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