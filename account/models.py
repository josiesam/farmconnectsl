from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headshot = models.ImageField(
            upload_to='userprofile/headshot', 
            blank=True, null=True,
            default='/default_profile.png'
            )
    bio = models.TextField(blank=True)
    locatiion = models.CharField(max_length=100, blank=True)
    is_farmer = models.BooleanField(default=False)

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
