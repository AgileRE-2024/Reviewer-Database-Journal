# admin.py
from django.contrib import admin
from .models import Reviewer, ScrapedPaper

@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ('name', 'paper_links')  # Menampilkan kolom paper_links di daftar Reviewer
    readonly_fields = ('paper_links',)  # Agar kolom ini muncul di halaman detail reviewer

admin.site.register(ScrapedPaper)
