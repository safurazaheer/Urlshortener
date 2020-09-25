from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UrlModel(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=50, blank=False, unique=True)
    original_url = models.URLField(max_length=1000, blank=False)

    def get_absolute_url(self):
        return reverse("myapp:url")

    def __str__(self):
        return str(self.creator) + str(self.keyword)

