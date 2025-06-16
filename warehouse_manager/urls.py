from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='warehouse-manager-home'),

    path('categories/', views.categories_management, name='warehouse-manager/categories'),
    path('products/', views.products_management, name='warehouse-manager/products'),
    path('product-details/', views.products_detail, name='warehouse-manager/product-details'),
    path('product-location/', views.product_location_management, name='warehouse-manager/product-location'),
    path('exports/', views.export_request, name='warehouse-manager/export-request'),
    path('imports/', views.import_management, name='warehouse-manager/import'),
]