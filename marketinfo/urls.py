from django.urls import path

from .views import (
    IndexView, BlogsView, EventsView,
    TipsView
)

app_name = 'marketinfo'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('events', EventsView.as_view(), name='events'),
    path('blogs', BlogsView.as_view(), name='blogs'),
    path('tips', TipsView.as_view(), name='tips')
]
