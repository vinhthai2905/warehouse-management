from datetime import datetime
from django.http import HttpResponse
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
    export_requests = DSYeuCauXuatKho.objects.filter(trang_thai__in=['Đã duyệt', 'Đã xuất'])

    for i, e_request in enumerate(export_requests):
        e_request: DSYeuCauXuatKho

        export_request_dict.append({
            'id': e_request.id_yeu_cau_xuat,
            'date': e_request.thoi_gian,
            'review_date': e_request.thoi_gian_duyet,
            'export_date': e_request.thoi_gian_xuat,
            'employee': e_request.id_nhan_vien_yc.ten_nhan_vien,
            'status': e_request.trang_thai
        })

    return render(request, 'sale_staff/export-request.html', context={
        'export_request_dict': export_request_dict
    })

# export_detail section
def export_detail(request):
    request_id = request.GET.get('request_id')
    request_employee = DSYeuCauXuatKho.objects.filter(id_yeu_cau_xuat=request_id).select_related('id_nhan_vien_yc').first()
    export_employee = HangXuatKho.objects.filter(id_yeu_cau_xuat=request_id).first()
    export_product_dict = list()

    export_products = ChiTietYeuCauXuat.objects.filter(id_yeu_cau_xuat=request_id).select_related('id_san_pham')

    export_info = {
        'request_date': request.GET.get('request_date'),
        'review_date': request.GET.get('review_date'),
        'export_date':  request.GET.get('export_date') if request.GET.get('export_date') is None else 'Chưa xác định',
        'request_employee': request_employee.id_nhan_vien_yc.ten_nhan_vien,
        'export_employee': export_employee.id_nhan_vien_xuat.ten_nhan_vien if export_employee else 'Chưa xác định',
        'status': request.GET.get('status')
    }
    for i, product in enumerate(export_products):
        product: ChiTietYeuCauXuat

        export_product_dict.append({
            'name': product.id_san_pham.ten_san_pham,
            'quantity': product.so_luong,
            'note': product.ghi_chu,
        })

    return render(request, 'sale_staff/export-detail.html', context={
        'export_info': export_info,
        'export_product_dict': export_product_dict

    })

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

    return redirect('export-request')
