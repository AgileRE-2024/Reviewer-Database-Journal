"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import DashboardPage
from .views import FavoritePage  
from .views import HistoryPage
from .views import LoginPage
from .views import SignupPage
from .views import UploadPaperPage
from .views import UploadDetailPage
from .views import ConfirmationPage
from .views import ReviewerPage
from .views import UploadOJSPage
from .views import ContactPage
from .views import scrape_reviewers
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', DashboardPage, name='dashboard'),
    path('favorites/', FavoritePage, name='favorites'),
    path('history/', HistoryPage, name='history'),
    path('', LoginPage, name='login'),
    path('signup/', SignupPage, name='signup'),
    path('upload/', UploadPaperPage, name='upload'),
    path('upload/detail/', UploadDetailPage, name='upload_detail'),
    path('confirmation/', ConfirmationPage, name='confirmation'),
    path('reviewer/', ReviewerPage, name='reviewer'),
    path('upload/ojs/', UploadOJSPage, name='upload_ojs'),
    path('contact/', ContactPage, name='contact'),
    path('scrape-reviewers/', scrape_reviewers, name='scrape_reviewers'),
]

