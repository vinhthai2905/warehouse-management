from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('employees/', views.employee_accounts, name='admin/employees'),

    path('employee/details', views.employee_infor, name='admin/employee-info')
]