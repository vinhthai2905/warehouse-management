from django.db import models
from django.db.models import ForeignKey
from django.views.decorators.http import condition


# Create your models here.

class SanPham(models.Model):
    idSanPham = models.CharField(
        primary_key=True,
        max_length=5,
        db_column='id_san_pham'
    )
    idDanhMuc = models.TextField(db_column='id_danh_muc')
    tenSanPham = models.TextField(db_column='ten_san_pham')
    soLuong = models.BigIntegerField(db_column='so_luong')
    moTa = models.TextField(db_column='mo_ta')
    trangThai = models.TextField(default='Không hỏng', db_column='trang_thai')
    hinhAnh = models.TextField(db_column='hinh_anh')
    donViTinh = models.TextField(default='Cái', db_column='don_vi_tinh')

    class Meta:
        db_table = 'san_pham'
        constraints = [
            models.CheckConstraint(
                check=models.Q(soLuong__gt=0),
                name='so_luong_lon_hon_0'
            )
        ]

class HangXuatKho(models.Model):
    idYeuCauXuat = models.CharField(
        primary_key=True,
        max_length=5,
        db_column='id_yeu_cau_xuat'
    )
    idSanPham = models.ForeignKey(
        SanPham,
        to_field='idSanPham',
        db_column='id_san_pham',
        on_delete=models.CASCADE
    )
    soLuong = models.IntegerField(db_column='so_luong')
    ghiChu = models.TextField(db_column='ghi_chu')
    thoiGianXuat = models.DateTimeField(db_column='thoi_gian_xuat')

    class Meta:
        db_table = 'hang_xuat_kho'

class DSYeuCauXuatKho(models.Model):
    idYeuCauXuat = models.CharField(
        primary_key=True,
        max_length=5,
        db_column='id_yeu_cau_xuat'
    )
    thoiGian = models.DateTimeField(db_column='thoi_gian')
    ghiChu = models.TextField(db_column='ghi_chu')
    trangThai = models.TextField(db_column='trang_thai')
    loai = models.TextField(db_column='loai')

    class Meta:
        db_table = 'ds_yeu_cau_xuat_kho'
        constraints = [
            models.CheckConstraint(
                check=models.Q(trangThai__in=[
                    'Chờ duyệt', 'Đã duyệt', 'Đã nhập kho', 'Từ chối'
                ]),
                name='trang_thai_hop_le'
            ),
            models.CheckConstraint(
                check=models.Q(loai__in=['Xuất hàng hỏng', 'Hàng để bán']),
                name='loai_hop_le'
            )
        ]

class ChiTietYeuCauXuat(models.Model):
    idYeuCauXuat = models.CharField(
        max_length=5,
        db_column='id_yeu_cau_xuat'
    )
    idSanPham = models.ForeignKey(
        SanPham,
        to_field='idSanPham',
        db_column='id_san_pham',
        on_delete=models.CASCADE
    )
    soLuong = models.IntegerField(db_column='so_luong')
    ghiChu = models.TextField(db_column='ghi_chu')

    class Meta:
        db_table = 'chi_tiet_yeu_cau_xuat'
        constraints = [
            models.UniqueConstraint(
                fields=['idYeuCauXuat', 'idSanPham'],
                name='pk_ctycx_composite'
            )
        ]


