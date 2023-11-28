from django.urls import path

from .views import LoginView, SignUpView, LogoutView, UserProfileEditView

app_name = 'account'

urlpatterns = [
     path('login', view=LoginView.as_view(), name='login'),
     path('signup', view=SignUpView.as_view(), name='signup'),
     path('logout', view=LogoutView.as_view(), name='logout'),
     path('profile/edit', view=UserProfileEditView.as_view(), name='user_profile_edit'),
     path('profile/change_password', view=UserProfileEditView.as_view(), name='change_password'),
]
