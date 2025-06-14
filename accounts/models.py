from django.db import models

# Create your models here.

class TaiKhoan(models.Model):
    id_nhan_vien = models.TextField(primary_key=True)
    ten_nhan_vien = models.TextField()
    mat_khau = models.TextField()
    chuc_vu = models.TextField()
    email = models.TextField()
    trang_thai = models.TextField()
    gioi_tinh = models.TextField()

    class Meta:
        db_table = 'tai_khoan'
        constraints = [
            models.CheckConstraint(
                check=models.Q(gioi_tinh__in = [
                    'Male', 'Female'
                ]),
                name='constraint_gioi_tinh'
            ),
            models.CheckConstraint(
                check=models.Q(chuc_vu__in = [
                    'Sale Staff', 'Warehouse Staff', 'Warehouse Manager', 'admin'
                ]),
                name='constraint_chuc_vu'
            )
        ]

