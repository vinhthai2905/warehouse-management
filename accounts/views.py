from django.shortcuts import render, redirect
from .models import TaiKhoan

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')

        try:
            user = TaiKhoan.objects.get(email=user_email, mat_khau=user_password)
            request.session['user_id'] = user.id_nhan_vien
            request.session['chuc_vu'] = user.chuc_vu

            if user.chuc_vu == 'Sale Staff':
                return redirect('products-info')
            if user.chuc_vu == 'Warehouse Staff':
                return redirect('warehouse-staff-home')
            if user.chuc_vu == 'Warehouse Manager':
                return redirect('warehouse-manager-home')
            if user.chuc_vu == 'admin' or user.chuc_vu == 'Admin':
                return redirect('admin-home')

        except TaiKhoan.DoesNotExist:
            return render(request, 'accounts/login.html', context={
                'error': 'Wrong email or password.'
            })


    return render(request, 'accounts/login.html', context={
    })


def log_out(request):
    request.session.flush()
    return redirect('log-in')



