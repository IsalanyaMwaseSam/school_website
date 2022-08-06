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
<<<<<<< HEAD
<<<<<<< HEAD
from education import views as education_views
=======
from users import views as user_views
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
=======
from users import views as user_views
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23




urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
    path('application/', education_views.application, name="application"),
    path('', include('education.urls')),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 


   
=======
=======
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
    path('', include('education.urls')),
    path('', include('users.urls')),
    path('users/register/', user_views.register, name='register'),
    path('users/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('users/profile/', user_views.profile, name='profile'),


]

if settings.DEBUG:
<<<<<<< HEAD
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
=======
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
