from django.contrib import admin
from .models import ScrapedPaper  # Import your ScrapedPaper model

admin.site.register(ScrapedPaper)  # Register the model to appear in admin