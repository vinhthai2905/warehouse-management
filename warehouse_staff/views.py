from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from accounts.models import TaiKhoan
from sale_staff.models import DSYeuCauXuatKho, ChiTietYeuCauXuat, SanPham, HangXuatKho


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
    if request.session.get('chuc_vu') != 'Warehouse Staff':
        return redirect('log-in')

    return render(request, 'warehouse_staff/home.html', )


def inventory(request):
    return render(request, 'warehouse_staff/inventory.html')

def pro_location(request):
    return render(request, 'warehouse_staff/pro_location.html')


def export_request(request):
    export_request_dict = list()
    export_requests = DSYeuCauXuatKho.objects.filter(trang_thai__in=['Chờ duyệt', 'Đã duyệt', 'Hoá đơn lỗi'])

    for e_request in export_requests:
        export_request_dict.append({
            'id': e_request.id_yeu_cau_xuat,
            'request_date': e_request.thoi_gian,
            'request_employee': e_request.id_nhan_vien_yc.ten_nhan_vien,
            'type': e_request.loai,
            'status': e_request.trang_thai,
            'export_date': e_request.thoi_gian_xuat,
            'review_date': e_request.thoi_gian_duyet,
        })

    return render(request, 'warehouse_staff/export-confirm.html', context={
        'export_request_dict': export_request_dict
    })


def export_detail(request):
    request_id = request.GET.get('request_id')
    export_product_dict = list()
    export_request_detail = DSYeuCauXuatKho.objects.get(id_yeu_cau_xuat=request_id)
    products = ChiTietYeuCauXuat.objects.filter(id_yeu_cau_xuat=request_id)

    export_info = {
        'request_id': request_id,
        'request_date': export_request_detail.thoi_gian,
        'review_date': export_request_detail.thoi_gian_duyet,
        'request_employee': export_request_detail.id_nhan_vien_yc.ten_nhan_vien,
        'review_employee':
            export_request_detail.id_nhan_vien_duyet.ten_nhan_vien
            if export_request_detail.id_nhan_vien_duyet
            else 'Chưa xác định',
        'status': export_request_detail.trang_thai
    }

    for export_product in products:
        if export_product.so_luong > export_product.so_luong_thuc:
            note = f'Sản phẩm {export_product.id_san_pham.ten_san_pham} thiếu {export_product.so_luong - export_product.so_luong_thuc}'
        elif export_product.so_luong < export_product.so_luong_thuc:
            note = f'Sản phẩm {export_product.id_san_pham.ten_san_pham} dư {export_product.so_luong_thuc - export_product.so_luong}'
        else:
            note = 'Đã nhận đủ'

        export_product_dict.append({
            'name': export_product.id_san_pham.ten_san_pham,
            'quantity': export_product.so_luong,
            'real_quantity': export_product.so_luong_thuc,
            'note': note
        })

    return render(request, 'warehouse_staff/export-detail.html', context={
        'export_info': export_info,
        'export_product_dict': export_product_dict
    })


@require_POST
def export_review(request):
    request_id = request.POST.get('request_id')

    request_record = DSYeuCauXuatKho.objects.get(id_yeu_cau_xuat=request_id)
    request_record.trang_thai = 'Đã duyệt'
    request_record.thoi_gian_duyet = datetime.now()
    request_record.save()

    return redirect('warehouse-staff/export-request')
