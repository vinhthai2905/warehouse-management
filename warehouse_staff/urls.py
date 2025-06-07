from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='warehouse-staff-home'),
    path('location/', views.pro_location, name='pro_location'),
    path('inventory/', views.inventory_management, name='inventory-management'),
    path('export/', views.export_management, name='export')
    # path ('export/test/', views.export_product, name='export-product'),
    # path('request-status/', views.request_status, name='request-status')


]