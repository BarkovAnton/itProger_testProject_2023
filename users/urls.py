from django.urls import path
from . import views as usersViews
from django.contrib.auth import views as djangoAuth

urlpatterns = [
    path('registr/', usersViews.registration, name='registration'),
    path('profile/', usersViews.profile, name='profile'),
    path('exit/', usersViews.logout_view, name='exit'),
    path('login/', djangoAuth.LoginView.as_view(template_name='users/login.html'), name='login'),
]