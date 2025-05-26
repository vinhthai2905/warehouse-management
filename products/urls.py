from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('export/', views.export_management, name='export'),
    path('info/', views.product_info, name='product_info'),

]