from django.views import View
from django.shortcuts import render

class LoginView(View):
    def get(self):
        return render(request=self.request, template_name='account/login.html')

class SignUpView(View):
    def get(self):
        return render(request=self.request, template_name='account/signup.html')
    

