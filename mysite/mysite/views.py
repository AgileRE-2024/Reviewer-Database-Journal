from django.shortcuts import render  


def DashboardPage(request):
    return render(request, 'dashboard.html')  

def FavoritePage(request):
    return render(request, 'favorite.html')  