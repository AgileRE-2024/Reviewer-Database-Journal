from django.shortcuts import render 
from django.http import JsonResponse
import pandas as pd
import requests
from myapp.models import ScrapedPaper  # Pastikan ScrapedPaper adalah model yang sudah didefinisikan

def scrape_reviewers(request):
    # Load the Excel file
    file_path = "C:\\Users\\Kevin\\Downloads\\USERS JISEBI.xlsx"
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        # Assuming column name is 'givenname.Element:Text'
        reviewer_names = df['givenname.Element:Text'].dropna().tolist()
        
        # Headers for the CrossRef API call
        headers = {
            'User-Agent': 'Postman'
        }

        # Make CrossRef API call for each reviewer name
        for name in reviewer_names:
            response = requests.get(
                f"https://api.crossref.org/works?query.author={name}",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                items = data.get('message', {}).get('items', [])
                
                for item in items:
                    title = item.get('title', ['No Title'])[0]
                    url = item.get('URL', 'No URL')
                    authors = item.get('author', [])
                    abstract = item.get('abstract', 'No Abstract')  # Extract abstract

                    # Extracting the first author name
                    first_author = ""
                    if authors:
                        first_author_data = authors[0]
                        first_author = f"{first_author_data.get('given', '')} {first_author_data.get('family', '')}".strip()
                    
                    # Check if entry already exists based on title or URL
                    if not ScrapedPaper.objects.filter(title=title, url=url).exists():
                        # Save the data to the database only if it does not already exist
                        ScrapedPaper.objects.create(
                            title=title,
                            url=url,
                            first_author=first_author,
                            abstract=abstract  # Save the abstract
                        )

                        # Print the filtered data to the terminal
                        print(f"Title: {title}")
                        print(f"URL: {url}")
                        print(f"First Author: {first_author}")

            else:
                # Print the error to the terminal
                print(f"Failed to fetch data for {name} (status code: {response.status_code})")

        # Return a success message
        return JsonResponse({'message': 'Scraping completed and data saved to the database'})

    except Exception as e:
        # Print the exception to the terminal
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