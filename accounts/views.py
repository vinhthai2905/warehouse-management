import requests
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
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
                return render(request, 'sale_staff/home.html', context={
                    'user_name': user.ten_nhan_vien
                })

        except TaiKhoan.DoesNotExist:
            return render(request, 'accounts/login.html', context={
                'error': 'Wrong email or password.'
            })


    return render(request, 'accounts/login.html', context={
    })


def log_out(request):
    request.session.flush()
    return redirect('log-in')



