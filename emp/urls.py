from django.urls import path
from emp.views import EmployeeCreateApp

urlpatterns = [
    path('', EmployeeCreateApp.as_view()),
]