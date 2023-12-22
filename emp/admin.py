from django.contrib import admin
from emp.models import Employee, Department
# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    ordering = ('id',)

admin.site.register(Department, DepartmentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id","employee_name", "department", "phone_number", "address","qualification")
    ordering = ('id',)
    # fields = ["employee_name", "department", "phone_number"]

admin.site.register(Employee, EmployeeAdmin)

