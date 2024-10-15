from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from .forms import ContactUsForm
from .models import Team, Affiliation, FAQ


class HomeView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='home')
        
        return render(self.request, 'core/home.html', context)


class AboutView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='about')

        return render(self.request, 'core/about.html', context)


class ContactView(View):
    context = {}
    def get(self, *args, **kwargs):
        form = ContactUsForm()
        self.context = {}
        self.context.update(location='contact', form=form)
        return render(self.request, "core/contact.html", self.context)
    
    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Sorry message not send')
            messages.info(self.request, 'You must be logged in to send a message')
            return redirect('contact')

        data = self.request.POST.copy()
        data['user'] = self.request.user.userprofile
        form = ContactUsForm(data)

        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            self.context.update({'form': form})
            return render(self.request, 'core/contact.html', self.context)
            
    
class TeamView(View):
    def get(self, *args, **kwargs):
        context = {}
        team = Team.objects.all()
        context.update(location='about', team=team)
        return render(self.request, "core/team.html", context)
    
class AffiliationView(View):
    def get(self, *args, **kwargs):
        context = {}
        affiliates = Affiliation.objects.all()
        context.update(location='about', affiliates=affiliates)

        return render(self.request, "core/affiliation.html", context)
    
class FAQView(View):
    def get(self, *args, **kwargs):
        context = {}
        faqs = FAQ.objects.all()[:10]
        context.update(faqs=faqs)
        return render(self.request, 'core/faq.html', context)
