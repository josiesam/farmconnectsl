

# urls.py
from django.urls import path
from .views import (
    IndexView, BlogIndexView, EventIndexView, TipIndexView,
    CropListView, CropDetailView, CropCreateView, CropUpdateView, CropDeleteView,
    # MarketPriceListView, MarketPriceDetailView, MarketPriceCreateView, MarketPriceUpdateView, MarketPriceDeleteView,
    # EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    # AttendeeListView, AttendeeDetailView, AttendeeCreateView, AttendeeUpdateView, AttendeeDeleteView,
    # BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView,
    # CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView,
    # UserSubmittedArticleListView, UserSubmittedArticleDetailView, UserSubmittedArticleCreateView,
    # UserSubmittedArticleUpdateView, UserSubmittedArticleDeleteView,
)

app_name = 'marketinfo'

urlpatterns = [
    # Sections' Index URLs
    path('', IndexView.as_view(), name='index'),
    path('events', EventIndexView.as_view(), name='events'),
    path('blogs', BlogIndexView.as_view(), name='blogs'),
    path('tips', TipIndexView.as_view(), name='tips'),

    # Crop URLs
    path('crops/', CropListView.as_view(), name='crop_list'),
    path('crops/<slug:slug>/', CropDetailView.as_view(), name='crop_detail'),
    path('crops/create/', CropCreateView.as_view(), name='crop_create'),
    path('crops/<slug:slug>/update/', CropUpdateView.as_view(), name='crop_update'),
    path('crops/<slug:slug>/delete/', CropDeleteView.as_view(), name='crop_delete'),

    # Repeat the above pattern for other models (MarketPrice, Event, Attendee, BlogPost, Comment, UserSubmittedArticle)
]
