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
<<<<<<< HEAD
<<<<<<< HEAD
    path('education/starter/', views.starter, name='starter'),
    
    
   
    
=======
=======
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
    path('education/application/', views.application, name='application'),
    path('education/starter/', views.starter, name='starter'),
    path('education/e-learning/', views.elearning, name='e-learning'),
    
    
<<<<<<< HEAD
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23
=======
>>>>>>> a9d900c1457080d90d61291d4e50f857aa62fa23

]