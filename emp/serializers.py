from emp.models import Department
from emp.models import Employee
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Department
        # fields = '__all__'
        fields = ["name"]


class EmployeeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Chain model """
    class Meta:
        model = Employee
        # fields = ['id', 'department', 'employee_name', 'surname', 'address', 'qualification', 'phone_number']
        fields = '__all__'
        # depth = 1