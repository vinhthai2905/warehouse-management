from datetime import datetime
from urllib.parse import urlencode

from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from accounts.models import TaiKhoan
from .models import SanPham, DSYeuCauXuatKho, ChiTietYeuCauXuat, HangXuatKho


# Create your views here.

def home(request):
    if request.session.get('chuc_vu') != 'Sale Staff':
        return redirect('log-in')  # or a custom 403 page
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
    export_requests = DSYeuCauXuatKho.objects.filter(trang_thai__in=['Đã duyệt', 'Đã xuất', 'Chờ duyệt'])

    for i, e_request in enumerate(export_requests):
        e_request: DSYeuCauXuatKho

        export_request_dict.append({
            'id': e_request.id_yeu_cau_xuat,
            'date': e_request.thoi_gian,
            'review_date': e_request.thoi_gian_duyet,
            'export_date': e_request.thoi_gian_xuat,
            'request_employee': e_request.id_nhan_vien_yc.ten_nhan_vien,
            'status': e_request.trang_thai
        })

    return render(request, 'sale_staff/export-request.html', context={
        'export_request_dict': export_request_dict
    })


def export_request_status(request):
    return render(request, 'sale_staff/export_request_status.html')


# export_detail section
def export_detail(request):
    request_id = request.GET.get('request_id')
    request_employee = DSYeuCauXuatKho.objects.filter(id_yeu_cau_xuat=request_id).select_related(
        'id_nhan_vien_yc').first()
    export_employee = HangXuatKho.objects.filter(id_yeu_cau_xuat=request_id).first()
    export_product_dict = list()

    export_products = ChiTietYeuCauXuat.objects.filter(id_yeu_cau_xuat=request_id).select_related('id_san_pham')

    export_info = {
        'request_date': request.GET.get('request_date'),
        'review_date': request.GET.get('review_date'),
        'export_date': request.GET.get('export_date')
        if request.GET.get('export_date') and request.GET.get('export_date') != 'None'
        else 'Chưa xác định',
        'request_employee': request_employee.id_nhan_vien_yc.ten_nhan_vien,
        'export_employee': export_employee.id_nhan_vien_xuat.ten_nhan_vien if export_employee else 'Chưa xác định',
        'status': request.GET.get('status'),
    }

    for i, product in enumerate(export_products):
        product: ChiTietYeuCauXuat

        export_product = {
            'id': product.id_san_pham_id,
            'name': product.id_san_pham.ten_san_pham,
            'quantity': product.so_luong,
            'real_quantity': product.so_luong_thuc,
            'note': product.ghi_chu,
        }

        if product.so_luong > product.so_luong_thuc:
            export_product['lack_quantity'] = product.so_luong - product.so_luong_thuc
        elif product.so_luong < product.so_luong_thuc:
            export_product['redundant_quantity'] = abs(product.so_luong - product.so_luong_thuc)

        export_product_dict.append(export_product)

    updated_products = [
        p for p in export_product_dict
        if 'lack_quantity' in p or 'redundant_quantity' in p
    ]

    return render(request, 'sale_staff/export-detail.html', context={
        'export_info': export_info,
        'export_product_dict': export_product_dict,
        'updated_products': updated_products
    })


@require_POST
def resend_export_request(request):
    request_id = request.POST.get('request_id')
    resend_export = DSYeuCauXuatKho.objects.get(id_yeu_cau_xuat=request_id)
    resend_export_products = ChiTietYeuCauXuat.objects.filter(id_yeu_cau_xuat=request_id)

    resend_export.id_nhan_vien_yc = TaiKhoan.objects.get(id_nhan_vien=request.session.get('user_id'))
    resend_export.thoi_gian = datetime.now()
    resend_export.trang_thai = 'Hoá đơn lỗi'

    for product in resend_export_products:
        product.so_luong_thuc = request.POST.get(f'real_quantity_{product.id_san_pham_id}')
        product.save()

    resend_export.save()

    query_params = urlencode({
        'request_id': request_id,
        'status': resend_export.trang_thai,
        'request_date': resend_export.thoi_gian,
        'review_date': resend_export.thoi_gian_duyet,
        'export_date': resend_export.thoi_gian_xuat or 'None',
    })

    messages.success(request, f'Gửi yêu cầu duyệt lại hóa đơn {request_id} thành công!')
    return redirect('export-request')


@require_POST
def export_confirm(request):
    request_id = request.POST.get('request_id')
    export_employee_id = request.POST.get('export_employee')
    export_employee = TaiKhoan.objects.get(id_nhan_vien=export_employee_id)
    export_items = ChiTietYeuCauXuat.objects.filter(id_yeu_cau_xuat=request_id)
    export_product_record = HangXuatKho

    for item in export_items:
        export_product_record.objects.create(
            id_yeu_cau_xuat=request_id,
            id_nhan_vien_xuat=export_employee,
            id_san_pham=item.id_san_pham,
            so_luong=item.so_luong,
            ghi_chu='Xuất tự động',
            thoi_gian_xuat=datetime.now()
        )
        product = item.id_san_pham
        product.so_luong -= item.so_luong
        product.save()

    request_record = DSYeuCauXuatKho.objects.get(id_yeu_cau_xuat=request_id)
    request_record.trang_thai = 'Đã xuất'
    request_record.thoi_gian_xuat = datetime.now()
    request_record.save()

    messages.success(request, f'Đã xuất hóa đơn {request_id} thành công!')
    return redirect('export-request')
