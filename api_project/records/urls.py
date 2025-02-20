from django.urls import path
from .views import home, about, register, experience, biography
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('experience/', experience, name='experience'),
    path('biography/', biography, name='biography'),
    path('register/', register, name='sign up'),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),
]
