# forms.py
from django import forms
from django.forms import ModelForm
from .models import Crop, MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle


class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
        }


class MarketPriceForm(ModelForm):
    class Meta:
        model = MarketPrice
        fields = ['crop', 'price']
        widgets = {
            'crop': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'time', 'registration_link']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'class': 'form-input'}),
            'date': forms.DateInput(attrs={'class': 'form-input'}),
            'time': forms.TimeInput(attrs={'class': 'form-input'}),
            'registration_link': forms.URLInput(attrs={'class': 'form-input'}),
        }


class AttendeeForm(ModelForm):
    class Meta:
        model = Attendee
        fields = ['event', 'user_profile', 'is_registered']
        widgets = {
            'event': forms.Select(attrs={'class': 'form-select'}),
            'user_profile': forms.Select(attrs={'class': 'form-select'}),
            'is_registered': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', ]
        widgets = {
            'post': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.HiddenInput(attrs={'class': 'form-select'}),
            'text': forms.Textarea(attrs={'class': 'form-input'}),
        }


class UserSubmittedArticleForm(ModelForm):
    class Meta:
        model = UserSubmittedArticle
        fields = ['title', 'content', 'author', 'is_approved']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
