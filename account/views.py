from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import (
    LoginForm, SignUpForm, UserProfileEditForm,
    UserEditForm, UserPasswordChangeForm
)


class LoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm

        context = {
            'form': form,
        }

        if self.request.user.is_authenticated:
            return redirect('home')

        return render(self.request, 'account/login.html', context)

    def post(self, *args, **kwargs):
        context = {}

        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        try:
            next = self.request.GET.get('next')
        except:
            next = None

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)

            if next:
                return redirect(next)

            return redirect('home')

        else:
            messages.error(self.request, 'Invalid credentials')
            form = LoginForm(self.request.POST)
            context.update({'form': form})

            return render(self.request, 'account/login.html', {'form': form})


class SignUpView(View):
    def get(self, *args, **kwargs):
        form = SignUpForm()
        context = {'form': form}
        return render(self.request, 'account/signup.html', context)

    def post(self, *args, **kwargs):
        context = {}
        data = self.request.POST.copy()
        form = SignUpForm(data)
        if form.is_valid():
            user = form.save()
            login(self.request, user)

            return redirect('home')

        else:
            context.update({'form': form})
            return render(self.request, 'account/signup.html', context)


class LogoutView(View):

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return redirect('home')


class UserProfileEditView(View):
    def get(self, *args, **kwargs):
        context = {}
        user = self.request.user
        profile = user.userprofile
        user_form = UserEditForm(instance=user)
        profile_form = UserProfileEditForm(instance=profile)
        context.update(
            user=user,
            profile=profile,
            user_form=user_form,
            profile_form=profile_form
        )

        return render(self.request, 'account/user-profile-edit.html', context)

    def post(self, *args, **kwargs):
        user = self.request.user
        profile = user.userprofile
        context = {
            'user': user,
            'profile': profile
        }
        data = self.request.POST.copy()
        user_data = {
            'username': data.get('username'),
            'firstname': data.get('first_name'),
            'last_name': data.get('last_name'),
            'email': data.get('email')
        }
        profile_data = {
            'headshot': data.get('headshot'),
            'bio': data.get('bio')
        }

        user_form = UserEditForm(user_data)
        profile_form = UserProfileEditForm(profile_data)

        if user_form.is_valid():
            user_form.save()
            if profile_form.is_valid():
                profile_form.save()
                messages.success(self.request, "Profile successfully updated")
                return redirect('account:user_profile')
            else:
                context.update(profile_form=profile_form)
                return render(self.request, 'account/user-profile-edit.html', context)
        else:
            context.update(user_form=user_form, profile_form=profile_form)
            return render(self.request, 'account/user-profile-edit.html', context)


class UserPasswordChangeView(View):
    def get(self, *args, **kwargs):
        context = {}
        form = UserPasswordChangeForm()
        context.update(form=form)

        return render(self.request, 'account/change-password.html', context)
    
    def post(self, *args, **kwargs):
        context = {}
        form = UserPasswordChangeForm(self.request.POST)

        if form.is_valid():
            form.save()
            messages.success(self.request, "Password successfully updated")
            
            return redirect('account:user_profile_edit')

        return 