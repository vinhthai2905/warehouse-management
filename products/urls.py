from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('info/', views.product_info, name='product_info'),
    path('inventory-management/', views.inventory_management, name='inventory-management'),
    path('export/', views.export_management, name='export'),
    path('request-status/', views.request_status, name='request-status')


]