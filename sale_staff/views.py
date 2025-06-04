from django.http import HttpResponse
from django.shortcuts import render
from .models import SanPham, DSYeuCauXuatKho

# Create your views here.


def home(request):
    products = list(SanPham.objects.all())
    product_dict = list()

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
    export_request_dict = list()
    export_requests = DSYeuCauXuatKho.objects.all()

    for i, e_request in enumerate(export_requests):
        e_request: DSYeuCauXuatKho

        export_request_dict.append({
            'id': e_request.idYeuCauXuat,
            'date': e_request.thoiGian,
            'employee': 'Vinh Thai',
            'status': e_request.trangThai
        })

    return render(request, 'sale_staff/export-request.html', context={
        'export_request_dict': export_request_dict
    })
def export_detail(request):
    return render(request, 'sale_staff/export-detail.html')



