from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length= 20)
    def __str__(self):
        return self.name

class Employee(models.Model):
    employee_name = models.CharField(max_length= 20)
    surname = models.CharField(max_length= 20)
    address = models.CharField(max_length  = 50)
    qualification = models.CharField(max_length = 30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.employee_name