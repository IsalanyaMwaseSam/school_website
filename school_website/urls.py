"""school_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:

"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('education.urls')),
    path('', include('users.urls')),
    path('users/register/', user_views.register, name='register'),
    path('users/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('users/profile/', user_views.profile, name='profile'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)