from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_info, name='product-info'),
    path('inventory/', views.inventory_management, name='inventory-management'),
    path('exports/', views.export_request, name='export-request'),
    path('export/details', views.export_detail, name='export-detail')


]