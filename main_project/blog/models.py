from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

