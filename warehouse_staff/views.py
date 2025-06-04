from django.http import HttpResponse
from django.shortcuts import render
from .models import SanPham
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
    return render(request, 'warehouse_staff/home.html', )

def export_management(request):
    return render(request, 'warehouse_staff/export-management.html')



def inventory_management(request):
    return render(request, 'warehouse_staff/inventory-management.html')

def pro_location(request):
    return render(request, 'warehouse_staff/pro_location.html')
