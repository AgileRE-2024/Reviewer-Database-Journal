# admin.py
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Reviewer, ScrapedPaper, DetailReviewer

@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ('name', 'detail_link', 'paper_links')  # Menampilkan kolom detail_link dan paper_links di daftar Reviewer
    readonly_fields = ('paper_links', 'detail_link')  # Agar kolom ini muncul di halaman detail reviewer

    def detail_link(self, obj):
        # Membuat link ke halaman DetailReviewer jika data tersedia
        if hasattr(obj, 'detail'):
            url = reverse('admin:myapp_detailreviewer_change', args=[obj.detail.id])
            return format_html('<a href="{}">View Details</a>', url)
        return "No Details"
    
    detail_link.short_description = "Reviewer Details"  # Nama kolom di halaman admin

# Register ScrapedPaper secara langsung, tanpa modifikasi tambahan
admin.site.register(ScrapedPaper)
admin.site.register(DetailReviewer)