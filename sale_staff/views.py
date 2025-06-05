from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import SanPham, DSYeuCauXuatKho, ChiTietYeuCauXuat


# Create your views here.


def home(request):
    products = list(SanPham.objects.all())
    product_dict = list()

    for i, product in enumerate(products):
        product: SanPham
        product_dict.append({
            'id': product.id_san_pham,
            'name': product.ten_san_pham,
            'category_id': product.id_danh_muc,
            'description': product.mo_ta,
            'status': product.trang_thai,
            'quantity': product.so_luong,
            'unit': product.don_vi_tinh
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
            'id': e_request.id_yeu_cau_xuat,
            'date': e_request.thoi_gian,
            'employee': 'Vinh Thai',
            'status': e_request.trang_thai
        })

    return render(request, 'sale_staff/export-request.html', context={
        'export_request_dict': export_request_dict
    })


# export_detail section
def export_detail(request):
    request_id = request.GET.get('request_id')
    export_product_dict = list()

    export_bills = ChiTietYeuCauXuat.objects.filter(id_yeu_cau_xuat=request_id).select_related('id_san_pham')

    export_info = {
        'date_request': request.GET.get('date'),
        'request_employee': 'Vinh Thai',
        'export_employee': 'Huyen Trang',
        'status': request.GET.get('status')
    }
    for i, export_bill in enumerate(export_bills):
        export_bill: ChiTietYeuCauXuat

        export_product_dict.append({
            'name': export_bill.id_san_pham.ten_san_pham,
            'quantity': export_bill.so_luong,
            'note': export_bill.ghi_chu,
        })

    return render(request, 'sale_staff/export-detail.html', context={
        'export_info': export_info,
        'export_product_dict': export_product_dict

    })

@require_POST
def confirm_export(request):
    request_id = request.POST.get('request_id')
    export_items = ChiTietYeuCauXuat.objects.filter(id_yeu_cau_xuat=request_id)

    for item in export_items:
        product = item.id_san_pham
        product.so_luong -= item.so_luong
        product.save()

    request_record = DSYeuCauXuatKho.objects.get(id_yeu_cau_xuat=request_id)
    request_record.trang_thai = 'Đã nhập kho'
    request_record.save()

    return redirect('export-request')
