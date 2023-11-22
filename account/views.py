from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, SignUpForm



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
            login(self.request,user)

            if next:
                return redirect(next)

            return redirect('home')

        else:
            messages.add_message(self.request, messages.ERROR, 'Invalid Credential')

            form = LoginForm(self.request.POST)
            context.update({'form': form})

            return render(self.request,'account/login.html',{'form':form})
     


class SignUpView(View):
    def get(self, *args, **kwargs):
        form = SignForm
        context = {'form': form}
        return render(self.request, 'account/signup.html')

    def post(self, *args, **kwargs):
        context = {}
        data = self.request.POST.copy()
        form = SignupForm(data)
        if form.is_valid():
            user = form.save()
            login(self.request, user)

            return redirect('home')
        
        else:
            context.update({'form': form})
            messages.error(self.request, str(form.errors))
            return render(self.request, 'account/signup.html', context)

    
class LogoutView(View):
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(request)
        return redirect('home')

