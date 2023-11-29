# forms.py
from django import forms
from django.forms import ModelForm
from .models import (
   Crop, CropEnvironment, CropEconomic,
   MarketPrice, 
   Event, Attendee, 
   BlogPost, Comment, UserSubmittedArticle
   )


class CropForm(ModelForm):
    class Meta:
        model = Crop
        fields = [
            'crop_type', 'crop_variety', 'planting_date', 'harvest_date',
            'yield_amount', 'units'
        ]
        widgets = {
            'crop_type': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'crop_variety': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'units': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'planting_date': forms.DateInput(attrs={
                'class': '''
                '''             
            }),
            'harvest_date': forms.DateInput(attrs={
                'class': '''
                '''             
            }),
            'yield_amount': forms.NumberInput(attrs={
                'class': '''
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500"
                '''             
            }),
        }

class CropEnvironmentForm(ModelForm):
    class Meta:
        model = CropEnvironment
        fields = [
            'crop', 'longitude', 'latitude', 'altitude' 
        ]
        widgets = {
            'crop': forms.HiddenInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'longitude': forms.NumberInput(attrs={
                'class': '''
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500"
                '''             
            }),
            'latitude': forms.NumberInput(attrs={
                'class': '''
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500"
                '''             
            }),
            'altitude': forms.NumberInput(attrs={
                'class': '''
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500"
                '''             
            }),
        }


class CropEconomicForm(ModelForm):
    class Meta:
        model = CropEconomic
        fields = [
            'crop', 'environment', 'cost_of_inputs', 'revenue',
        ]
        widgets = {
            'crop': forms.HiddenInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'environment': forms.HiddenInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'cost_of_inputs': forms.NumberInput(attrs={
                'class': '''
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500"
                '''             
            }),
            'revenue': forms.NumberInput(attrs={
                'class': '''
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500"
                '''             
            }),
        }


class MarketPriceForm(ModelForm):
    class Meta:
        model = MarketPrice
        fields = ['economic', 'price']
        widgets = {
            'economic': forms.Select(attrs={
                'class': """
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500
                """
                }),
            'price': forms.NumberInput(attrs={
                'class': '''
                    bg-gray-50 border border-gray-300 text-gray-900 text-sm 
                    rounded-lg focus:ring-blue-500 focus:border-blue-500 block 
                    w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                    dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 
                    dark:focus:border-blue-500"
                '''             
                }),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'time', 'registration_link']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'description': forms.Textarea(attrs={
                'class': """
                        block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg
                        border border-gray-300 focus:ring-blue-500 focus:border-blue-500 
                        dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                        dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
                    """            
            }),
            'location': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'date': forms.DateInput(attrs={'class': 'form-input'}),
            'time': forms.TimeInput(attrs={'class': 'form-input'}),
            'registration_link': forms.URLInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
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
            'title': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'content': forms.Textarea(attrs={
                'class': """
                        block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg
                        border border-gray-300 focus:ring-blue-500 focus:border-blue-500 
                        dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                        dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
                    """             
            }),
            'author': forms.HiddenInput(attrs={
                'class': ''
                }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', ]
        widgets = {
            'post': forms.HiddenInput(attrs={
                'class': ''
                }),
            'user': forms.HiddenInput(attrs={
                'class': ''
                }),
            'text': forms.Textarea(attrs={
                'class': """
                        block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg
                        border border-gray-300 focus:ring-blue-500 focus:border-blue-500 
                        dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                        dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
                    """           
            }),
        }


class UserSubmittedArticleForm(ModelForm):
    class Meta:
        model = UserSubmittedArticle
        fields = ['title', 'content', 'author', 'is_approved']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'content': forms.Textarea(attrs={
                'class': """
                        block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg
                        border border-gray-300 focus:ring-blue-500 focus:border-blue-500 
                        dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                        dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
                    """           
            }),
            'author': forms.HiddenInput(attrs={
                'class': ''
                }),
            'is_approved': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
