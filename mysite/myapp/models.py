from django.db import models

class ScrapedPaper(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()
    first_author = models.CharField(max_length=255)
    abstract = models.TextField(blank=True, null=True)  # New abstract field

    def __str__(self):
        return f"{self.title} by {self.first_author}"