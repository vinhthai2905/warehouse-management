from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.views.decorators.http import condition
from accounts.models import TaiKhoan


# Create your models here.

class SanPham(models.Model):
    id_san_pham = models.CharField(
        primary_key=True,
        max_length=5,
        db_column='id_san_pham'
    )
    id_danh_muc = models.TextField(db_column='id_danh_muc')
    ten_san_pham = models.TextField(db_column='ten_san_pham')
    so_luong = models.BigIntegerField(db_column='so_luong')
    mo_ta = models.TextField(db_column='mo_ta')
    trang_thai = models.TextField(default='Không hỏng', db_column='trang_thai')
    hinh_anh = models.TextField(db_column='hinh_anh')
    don_vi_tinh = models.TextField(default='Cái', db_column='don_vi_tinh')

    class Meta:
        db_table = 'san_pham'
        constraints = [
            models.CheckConstraint(
                check=models.Q(so_luong__gt=0),
                name='so_luong_lon_hon_0'
            )
        ]

class HangXuatKho(models.Model):
    id_yeu_cau_xuat = models.CharField(
        max_length=5,
        db_column='id_yeu_cau_xuat'
    )
    id_nhan_vien_xuat = models.ForeignKey(
        TaiKhoan,
        to_field='id_nhan_vien',
        db_column='id_nhan_vien_xuat',
        on_delete=models.CASCADE
    )
    id_san_pham = models.ForeignKey(
        SanPham,
        to_field='id_san_pham',
        db_column='id_san_pham',
        on_delete=models.CASCADE
    )
    so_luong = models.IntegerField(db_column='so_luong')
    ghi_chu = models.TextField(db_column='ghi_chu')
    thoi_gian_xuat = models.DateTimeField(db_column='thoi_gian_xuat')

    class Meta:
        db_table = 'hang_xuat_kho'
        constraints = [
            models.UniqueConstraint(
                fields=['id_yeu_cau_xuat', 'id_san_pham'],
                name='primary_key_id_yc_id_san_pham'
            )
        ]

class DSYeuCauXuatKho(models.Model):
    id_yeu_cau_xuat = models.CharField(
        primary_key=True,
        max_length=5,
        db_column='id_yeu_cau_xuat'
    )
    id_nhan_vien_yc = models.ForeignKey(
        TaiKhoan,
        to_field='id_nhan_vien',
        db_column='id_nhan_vien_yc',
        related_name='yeu_cau_xuat_yc',
        on_delete=CASCADE,
    )
    id_nhan_vien_duyet = models.ForeignKey(
        TaiKhoan,
        to_field='id_nhan_vien',
        db_column='id_nhan_vien_duyet',
        related_name='yeu_cau_xuat_duyet',
        null=True,
        on_delete=CASCADE
    )
    # id_nhan_vien_xuat = models.ForeignKey(
    #     TaiKhoan,
    #     to_field='id_nhan_vien',
    #     db_column='id_nhan_vien_xuat',
    #     on_delete=CASCADE
    # )
    thoi_gian = models.DateTimeField(db_column='thoi_gian')
    thoi_gian_xuat = models.DateTimeField(null=True)
    thoi_gian_duyet = models.DateTimeField(null=True)
    ghi_chu = models.TextField(db_column='ghi_chu')
    trang_thai = models.TextField(db_column='trang_thai')
    loai = models.TextField(db_column='loai')

    class Meta:
        db_table = 'ds_yeu_cau_xuat_kho'
        constraints = [
            models.CheckConstraint(
                check=models.Q(trang_thai__in=[
                    'Chờ duyệt', 'Đã duyệt', 'Đã xuất', 'Từ chối'
                ]),
                name='trang_thai_hop_le'
            ),
            models.CheckConstraint(
                check=models.Q(loai__in=['Xuất hàng hỏng', 'Hàng để bán']),
                name='loai_hop_le'
            )
        ]

class ChiTietYeuCauXuat(models.Model):
    id_yeu_cau_xuat = models.CharField(
        max_length=5,
        db_column='id_yeu_cau_xuat'
    )
    id_san_pham = models.ForeignKey(
        SanPham,
        to_field='id_san_pham',
        db_column='id_san_pham',
        on_delete=models.CASCADE
    )
    so_luong = models.IntegerField(db_column='so_luong')
    ghi_chu = models.TextField(db_column='ghi_chu')

    class Meta:
        db_table = 'chi_tiet_yeu_cau_xuat'
        constraints = [
            models.UniqueConstraint(
                fields=['id_yeu_cau_xuat', 'id_san_pham'],
                name='pk_ctycx_composite'
            )
        ]


