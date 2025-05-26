from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    section = request.GET.get('section')
    if section == 'export-management':
        context['show_export_management'] = True
    elif section == 'inventory-management':
        context['show_inventory_management'] = True
    elif section == 'product-info':
        context['show_product_info'] = True
    return render(request, 'products/home.html', context)