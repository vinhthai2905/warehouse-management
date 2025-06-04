from django.http import HttpResponse
from django.shortcuts import render
from .models import SanPham

# Create your views here.


def home(request):

    products = list(SanPham.objects.all())
    product_dict = list()
    test = dict()

    for i, product in enumerate(products):
        product: SanPham
        product_dict.append({
            'id': product.idSanPham,
            'name': product.tenSanPham,
            'category_id': product.idDanhMuc,
            'description': product.moTa,
            'status': product.trangThai,
            'quantity': product.soLuong,
            'unit': product.donViTinh
        })

    return render(request, 'sale_staff/home.html', {
        'product_dict': product_dict
    })

def product_info(request):
    return render(request, 'sale_staff/product-info.html')
def inventory_management(request):
    return render(request, 'sale_staff/inventory-management.html')
def export_request(request):
    return render(request, 'sale_staff/export-request.html')
def request_status(request):
    return render(request, 'sale_staff/export-detail.html')



