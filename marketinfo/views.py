from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Crop, MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle
from .forms import CropForm, MarketPriceForm, EventForm, AttendeeForm, BlogPostForm, CommentForm, UserSubmittedArticleForm
from django.urls import reverse_lazy

# ========================= Index View =========================
class IndexView(View):
    def get(self, *arg, **kwargs):
        return redirect('marketinfo:crop_list')


class EventIndexView(View):
    def get(self, *args, **kwargs):
        return redirect('marketinfo:event_list')


class BlogIndexView(View):
    def get(self, *args, **kwargs):
        return redirect('marketinfo:blogpost_list')


class TipIndexView(View):
    def get(self, *args, **kwargs):
        context = {}
        context.update(location='marketinfo')
        return render(self.request, 'marketinfo/tips.html', context)

# ========================= End Index View =========================

# ========================= BlogPost CRUD View =========================
class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'marketinfo/blogpost/blogpost_form.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blogpost_list')


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'marketinfo/blogpost/blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context.update(location='blog')
        print(context)
        return context


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'marketinfo/blogpost/blogpost_list.html'
    context_object_name = 'blogposts'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        blogposts = BlogPost.objects.all()
        context.update(location='blog', blogposts=blogposts)
        return context


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blogpost/blogpost_form.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('blogpost_list')



# ========================= End BlogPost CRUD View =========================




# ========================= Crop CRUD View =========================
class CropCreateView(CreateView):
    model = Crop
    template_name = 'marketinfo/crop/crop_form.html'
    form_class = CropForm
    success_url = reverse_lazy('crop_list')


class CropDeleteView(DeleteView):
    model = Crop
    template_name = 'crop/crop_confirm_delete.html'
    success_url = reverse_lazy('crop_list')


class CropDetailView(DetailView):
    model = Crop
    template_name = 'marketinfo/crop/crop_detail.html'
    context_object_name = 'crop'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        crop = self.get_object()
        context.update(location='marketinfo', fields=crop._meta.fields)
        return context


class CropListView(ListView):
    model = Crop
    template_name = 'marketinfo/crop/crop_list.html'
    context_object_name = 'crops'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context.update(location='marketinfo')
        return context


class CropUpdateView(UpdateView):
    model = Crop
    template_name = 'crop/crop_form.html'
    form_class = CropForm
    success_url = reverse_lazy('crop_list')



# ========================= End Crop CRUD View =========================


# ========================= Event CRUD View =========================
class EventCreateView(CreateView):
    model = Event
    template_name = 'marketinfo/event/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('event_list')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'marketinfo/event/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')


class EventDetailView(DetailView):
    model = Event
    template_name = 'marketinfo/event/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context.update(location='blog')
        print(context)
        return context


class EventListView(ListView):
    model = BlogPost
    template_name = 'marketinfo/event/event_list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        events = Event.objects.all()
        context.update(location='event', events=events)
        return context


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'marketinfo/event/event_form.html'
    form_class = EventForm
    success_url = reverse_lazy('event_list')



# ========================= End Event CRUD View =========================







class MarketpriceListView(ListView):
    model = MarketPrice
    template_name = 'marketprice/marketprice_list.html'
    context_object_name = 'marketprices'


class MarketPriceDetailView(DetailView):
    model = MarketPrice
    template_name = 'marketprice/marketprice_detail.html'
    context_object_name = 'marketprice'


class MarketPriceCreateView(CreateView):
    model = MarketPrice
    template_name = 'marketprice/marketprice_form.html'
    form_class = MarketPriceForm
    success_url = reverse_lazy('marketprice_list')


class MarketPriceUpdateView(UpdateView):
    model = MarketPrice
    template_name = 'marketprice/marketprice_form.html'
    form_class = MarketPriceForm
    success_url = reverse_lazy('marketprice_list')


class MarketPriceDeleteView(DeleteView):
    model = MarketPrice
    template_name = 'marketPrice/marketprice_confirm_delete.html'
    success_url = reverse_lazy('marketPrice_list')

# Repeat the above pattern for other models (MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle)

