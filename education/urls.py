from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/computing/', views.computing, name='Computing'),
    path('education/business/', views.business, name='business'),
    path('education/education/', views.education, name='education'),
    path('education/graduation/', views.graduation, name='graduation'),
    path('education/growth/', views.growth, name='growth'),
    path('education/health/', views.health, name='health'),
    path('education/research/', views.research, name='research'),
    path('education/social/', views.social, name='social'),
    path('education/theology/', views.theology, name='theology'),
    path('education/About_us/', views.about, name='about'),
    path('education/starter/', views.starter, name='starter'),
    
    
   
    

]