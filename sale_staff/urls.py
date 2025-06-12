from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='sale-staff-home'),
    path('products/', views.product_info, name='products-info'),
    path('inventory/', views.inventory_management, name='inventory-management'),
    path('exports/', views.export_request, name='export-request'),
    path('export/details', views.export_detail, name='export-detail'),
    path('export/details/resend', views.resend_export_request, name='resend-export-request'),
    path('export/confirm', views.export_confirm, name='export-confirm'),
    path('export-status', views.export_request_status)

]