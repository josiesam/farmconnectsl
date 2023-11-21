from django.urls import path

from .views import LoginView, SignUpView

urlpatterns = [
     path('login', view=LoginView.as_view()),
     path('signup', view=SignUpView.as_view()),
]
