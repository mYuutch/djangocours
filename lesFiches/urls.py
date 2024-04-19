from django.urls import path
from . import views

urlpatterns=[
    path('home', views.home,name='home'),
    path('home/<film>', views.home,name='home'),
    path('films', views.films, name='films'),
    path('acteurs', views.acteurs,name='acteurs'),
    path('realisateurs', views.realisateurs,name='realisateurs'),
    path('add', views.formu, name='formu'),
]