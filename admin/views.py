from django.shortcuts import render, get_object_or_404
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

    return render(request, 'admin/account-management/employee-account.html', context={
        'accounts_dict': accounts_dict
    })


def employee_infor(request):
    emp_id = request.GET.get('id')
    employee = get_object_or_404(TaiKhoan, id_nhan_vien=emp_id)

    context = {
        'employee': {
            'id': employee.id_nhan_vien,
            'name': employee.ten_nhan_vien,
            'role': employee.chuc_vu,
            'username': employee.email,
            'sex': employee.gioi_tinh,
        }
    }

    return render(request, 'admin/account-management/employee-info.html', context=context)
