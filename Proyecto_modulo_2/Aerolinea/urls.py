from django.contrib import admin
from django.urls import path, include
from Aerolinea import views

urlpatterns = [
    path('home', views.home, name= 'home'),
    path('purchase', views.purchase),
    path('reservation', views.reservation),
    
    
]
