from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    
    path('', views.index, name='index'),   
    path("home", views.home,name='home'),
]