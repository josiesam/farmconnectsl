from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm

from .models import UserProfile

class LoginForm(AuthenticationForm):
    username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                )
            )
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                )
            )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                )
            )
    last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                )
            )
    username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                )
            )
    email = forms.EmailField(
            max_length=254, 
            required=True, 
            help_text='Required. Enter a valid email address.',
            widget=forms.EmailInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                ), 
            )
    password1 = forms.CharField(
            label="Password", 
            widget=forms.PasswordInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                )
            )
    password2 = forms.CharField(
            label="Password Confirmation", 
            widget=forms.PasswordInput(
                attrs={
                    'class': """
                        bg-gray-50 border border-gray-300 text-gray-900 
                        text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 
                        block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 
                        dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500
                        dark:focus:border-blue-500
                    """
                    }
                )
            )
    is_farmer = forms.BooleanField(
            required=False,
            widget=forms.CheckboxInput(
                attrs={
                    'class': """
                        w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 
                        rounded focus:ring-blue-500 dark:focus:ring-blue-600 
                        dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700
                        dark:border-gray-600
                    """
                    }    
                )
            )

    class Meta:
        model = User
        fields = (
                'username', 'first_name', 'last_name', 
                'email', 'password1', 'password2', 
                'is_farmer'
            )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'first_name': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''
            }),
            'last_name': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),
            'email': forms.EmailInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            })
        }

class UserProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('headshot', 'bio', 'address')
        widgets = {
            'address': forms.TextInput(attrs={
                'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
                '''             
            }),

        }


class UserPasswordResetForm(PasswordResetForm):
    pass

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={
            'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
            '''
        })
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
            '''
        })
    )
    new_password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': '''
                    shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg
                    focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 
                    dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 
                    dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500
            '''
        })
    )