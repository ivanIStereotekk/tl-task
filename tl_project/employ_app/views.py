from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Department, Employee

def department_list(request):
    """Вывод списка подразделений в древовидном формате"""
    departments = Department.objects.all()
    return render(request, 'company/department.html', {'departments': departments})

def employee_list(request, department_id):
    """Вывод сотрудников конкретного подразделения"""
    department = get_object_or_404(Department, id=department_id)
    employees = department.employees.all()
    data = [{"id": emp.pk, "full_name": emp.full_name, "position": emp.position} for emp in employees]
    return JsonResponse(data, safe=False)
