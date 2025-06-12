from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='warehouse-staff-home'),
    path('location/', views.pro_location, name='pro_location'),
    path('inventory/', views.inventory, name='warehouse-staff/inventory'),
    path('exports/', views.export_request, name='warehouse-staff/export-request'),
    path('export/details', views.export_detail, name='warehouse-staff/export-detail'),
    path('export/review', views.export_review, name='warehouse-staff/export-review'),
    path('defective/', views.defective_products, name='warehouse-staff/defective-products'),
    path('location-products/', views.location_products, name='warehouse-staff/location-products'),


]