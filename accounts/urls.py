from django.shortcuts import redirect, render
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='log-in'),
    path('logout', views.log_out, name='log-out'),
]
