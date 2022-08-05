from django.urls import path
from . import views

urlpatterns = [
    path('users/course/', views.course, name='course'),
    path('users/staff/', views.staff, name='staff')
]