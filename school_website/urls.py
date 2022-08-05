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
from education import views as education_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('application/', education_views.application, name="application"),
    path('', include('education.urls')),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


   