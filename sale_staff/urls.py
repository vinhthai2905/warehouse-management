from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_info, name='product-info'),
    path('inventory/', views.inventory_management, name='inventory-management'),
    path('export/', views.export_request, name='export-request'),
    path('request-status/', views.request_status, name='request-status')


]