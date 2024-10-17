from django.shortcuts import render  


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