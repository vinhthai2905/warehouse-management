# Generated by Django 5.1.3 on 2025-06-10 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('sale_staff', '0003_chitietyeucauxuat_so_luong_thuc'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='dsyeucauxuatkho',
            name='trang_thai_hop_le',
        ),
        migrations.AddConstraint(
            model_name='dsyeucauxuatkho',
            constraint=models.CheckConstraint(condition=models.Q(('trang_thai__in', ['Chờ duyệt', 'Đã duyệt', 'Đã xuất', 'Từ chối', 'Hoá đơn lỗi'])), name='trang_thai_hop_le'),
        ),
    ]
