from django.db import models
from django.utils import timezone

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='Photos')
    img_thumb = models.ImageField(upload_to='Photos/thumbnails')
    instagram = models.URLField(default="https://www.instagram.com/")

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=32)
    profile_instagram = models.URLField(default="https://www.instagram.com/")
    page_instagram = models.URLField(default="https://www.instagram.com/")
    twitter = models.URLField(default="https://twitter.com")
    facebook = models.URLField(default="https://www.facebook.com/")
    email = models.URLField(default="https://www.google.com/")
    profile_picture = models.ImageField(upload_to='Profile')
    index_background = models.ImageField(upload_to='Profile')
    profile_description = models.TextField()
    developer_website = models.URLField(default="https://www.google.com/")

    def __str__(self):
        return self.name