from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register", views.register, name = 'user-register-page'),
    path("profile", views.profile, name = 'user-profile-page'),
    path("login", LoginView.as_view(template_name='user/login.html'), name = 'user-login-page'),
    path("logout", LogoutView.as_view(template_name='user/logout.html'), name = 'user-logout-page'),
]