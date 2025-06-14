from django.shortcuts import render
from sale_staff.models import TaiKhoan
# Create your views here.

def home(request):
    return render(request, 'admin/home.html')

def employee_accounts(request):
    accounts_dict = list()
    employee_query = TaiKhoan.objects.all()

    for employee in employee_query:
        accounts_dict.append({
            'id': employee.id_nhan_vien,
            'name': employee.ten_nhan_vien,
            'role': employee.chuc_vu,
            'email': employee.email,
            'status': employee.trang_thai,
            'sex': employee.gioi_tinh,
        })

    return render(request, 'admin/account-management/user-account.html', context={
        'accounts_dict': accounts_dict
    })
