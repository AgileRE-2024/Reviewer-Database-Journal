from django.db import models

# models.py
from django.urls import reverse
from django.utils.html import format_html

class Reviewer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def paper_links(self):
        # Membuat link untuk setiap judul paper
        links = [
            format_html(
                '<a href="{}">{}</a>',
                reverse('admin:myapp_scrapedpaper_change', args=[paper.id]),
                paper.title
            ) for paper in self.papers.all()
        ]
        return format_html("<br>".join(links))

    paper_links.short_description = "Paper Titles"  # Nama kolom di halaman admin

class ScrapedPaper(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()
    first_author = models.CharField(max_length=255)
    abstract = models.TextField(blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='papers')
    
    def __str__(self):
        return f"{self.title} by {self.first_author}"


