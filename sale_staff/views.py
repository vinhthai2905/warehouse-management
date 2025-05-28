from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, 'sale_staff/home.html')

def product_info(request):
    return render(request, 'sale_staff/product-info.html')
def inventory_management(request):
    return render(request, 'sale_staff/inventory-management.html')
def export_request(request):
    return render(request, 'sale_staff/export-request.html')
def request_status(request):
    return render(request, 'sale_staff/status-management.html')



