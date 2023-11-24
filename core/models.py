from django.db import models

class ContactUs(models.Model):
    user = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    