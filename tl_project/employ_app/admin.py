from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Department, Employee

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    pass

class EmployeeAdmin(admin.ModelAdmin):
    pass



admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)

