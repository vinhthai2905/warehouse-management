from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'warehouse_staff/home.html', )

def export_management(request):
    return render(request, 'warehouse_staff/export-management.html')


def inventory_management(request):
    return render(request, 'warehouse_staff/inventory-management.html')

def pro_location(request):
    return render(request, 'warehouse_staff/pro_location.html')
