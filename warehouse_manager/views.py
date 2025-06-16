from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

# Create your views here.

def home(request):
    # context = {}
    # section = request.GET.get('section')
    # if section == 'export-management':
    #     context['show_export_management'] = True
    # elif section == 'inventory-management':
    #     context['show_inventory_management'] = True
    # elif section == 'product-info':
    #     context['show_product_info'] = True
    # if request.session.get('chuc_vu') != 'Warehouse Manager':
    #     return redirect('log-in')

    return render(request, 'warehouse_manager/home.html', )

def product_management(request):
    return render(request, 'warehouse_manager/product-management.html')

def categories_management(request):
    return render(request, 'warehouse_manager/product-management/category.html')

def products_management(request):
    return render(request, 'warehouse_manager/product-management/product.html')

def product_location_management(request):
    return render(request, 'warehouse_manager/product-management/product-location.html')

def products_detail(request):
    return render(request, 'warehouse_manager/product-management/product-detail.html')
def import_management(request):
    return render(request, 'warehouse_manager/product-management/import-management.html')

def export_request(request):
    return render(request, 'warehouse_manager/export-request.html')
