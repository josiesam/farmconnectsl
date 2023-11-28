from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Crop, MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle
from .forms import CropForm, MarketPriceForm, EventForm, AttendeeForm, BlogPostForm, CommentForm, UserSubmittedArticleForm
from django.urls import reverse_lazy

# Create your views here.


class IndexView(View):
    def get(self, *arg, **kwargs):
        context = {}
        context.update(location='marketinfo')
        return render(self.request, 'marketinfo/index.html', context)


class EventsView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='event')
        return render(self.request, 'marketinfo/events.html', context)


class BlogsView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='blog')
        return render(self.request, 'marketinfo/blogs.html', context)


class TipsView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='marketinfo')

        return render(self.request, 'marketinfo/tips.html', context)


class CropListView(ListView):
    model = Crop
    template_name = 'crop/crop_list.html'
    context_object_name = 'crops'


class CropDetailView(DetailView):
    model = Crop
    template_name = 'crop/crop_detail.html'
    context_object_name = 'crop'


class CropCreateView(CreateView):
    model = Crop
    template_name = 'crop/crop_form.html'
    form_class = CropForm
    success_url = reverse_lazy('crop_list')


class CropUpdateView(UpdateView):
    model = Crop
    template_name = 'crop/crop_form.html'
    form_class = CropForm
    success_url = reverse_lazy('crop_list')


class CropDeleteView(DeleteView):
    model = Crop
    template_name = 'crop/crop_confirm_delete.html'
    success_url = reverse_lazy('crop_list')


# Repeat the above pattern for other models (MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle)

