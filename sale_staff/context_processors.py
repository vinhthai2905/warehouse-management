from accounts.models import TaiKhoan

def user_info(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:
            user = TaiKhoan.objects.get(id_nhan_vien=user_id)
            context = {
                'user_name': user.ten_nhan_vien,
                'user_role': user.chuc_vu,
                'user_email': user.email,
            }
        except TaiKhoan.DoesNotExist:
            pass
    return context