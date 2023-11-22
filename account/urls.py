from django.urls import path

from .views import LoginView, SignUpView, LogoutView

app_name = 'account'

urlpatterns = [
     path('login', view=LoginView.as_view(), name='login'),
     path('signup', view=SignUpView.as_view(), name='signup'),
     path('logout', view=LogoutView.as_view(), name='logout'),
]
