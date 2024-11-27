# models.py
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

class Reviewer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def paper_links(self):
        links = [
            format_html(
                '<a href="{}">{}</a>',
                reverse('admin:myapp_scrapedpaper_change', args=[paper.id]),
                paper.title
            ) for paper in self.papers.all()
        ]
        return format_html("<br>".join(links))

    paper_links.short_description = "Paper Titles"  # Nama kolom di halaman admin


class DetailReviewer(models.Model):
    reviewer = models.OneToOneField(Reviewer, on_delete=models.CASCADE, related_name='detail')
    country = models.CharField(max_length=255, default='NULL')
    email = models.EmailField(max_length=255, default='NULL')
    orcid = models.CharField(max_length=255, default='NULL')
    username = models.CharField(max_length=255, default='NULL')
    affiliation = models.TextField(blank=True, null=True)  # Tambahkan kolom afiliasi

    def __str__(self):
        return f"Detail of {self.reviewer.name}"


class ScrapedPaper(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()
    authors = models.TextField(null=True)  # Mengubah kolom first_author menjadi authors
    abstract = models.TextField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)  # Kolom baru untuk publisher
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='papers')
    
    def __str__(self):
        return f"{self.title} by {self.authors}"
