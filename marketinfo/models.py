from django.db import models

# Create your models here.
from django.db import models



class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

# You can add more fields like optimal growing conditions, etc.


class MarketPrice(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    registration_link = models.URLField(blank=True, null=True)


class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        'account.UserProfile', on_delete=models.CASCADE)
    is_registered = models.BooleanField(default=False)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class UserSubmittedArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
