from django.urls import path
from .views import department_list, employee_list

urlpatterns = [
    path('departments/', department_list, name='department_list'),
    path('departments/<int:department_id>/employees/', employee_list, name='employee_list')
]
