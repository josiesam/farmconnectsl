from django.db import models

class ContactUs(models.Model):
    user = models.ForeignKey('account.UserProfile', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='team/profile')
    bio = models.TextField()
    organization = models.CharField(max_length=2000) 
    role = models.CharField(max_length=2000)  
    
    def __str__(self):
        return f'{self.name}'

class Affiliation(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='affiliation/logo')
    def __str__(self):
        return f'{self.name}'

class FAQ(models.Model):
    topic = models.CharField(max_length=100)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    
