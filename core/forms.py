from django import forms

from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('user', 'subject', 'message')
        widgets = {
            'user': forms.HiddenInput(),
            'subject': forms.TextInput(attrs={
                'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
            }),
            'message': forms.Textarea(attrs={
                'class': """
                        block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg
                        border border-gray-300 focus:ring-blue-500 focus:border-blue-500 
                        dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                        dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500
                    """
            })
        }