from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from emp.serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework import status
from django.http import JsonResponse
from emp.models import *
# Create your views here.
authentication_classes = [authentication.TokenAuthentication]
permission_classes = [permissions.IsAdminUser]

class EmployeeCreateApp(APIView):

    def get(self, request,  *args, **kwargs):
        id_param = request.query_params.get('id', None)
        if id_param is not None:
            try:
                instance = Employee.objects.get(id=id_param)
                serializer = EmployeeSerializer(instance)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return JsonResponse({'error': 'Not found'}, status=404)
        else:
            queryset = Employee.objects.all()
            serializer = EmployeeSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        try:
            data = request.data
            department_id = Department.objects.get(name=data.get("department"))
            data ["department"] = department_id.id
            emp_serializer = EmployeeSerializer(data=data)
            print(emp_serializer.is_valid())
            if emp_serializer.is_valid():
                emp_serializer.save()
                data_response = {
                    "message":"Employee created success.",
                    "success" : True,
                    "result" : emp_serializer.data,
                    "status" : status.HTTP_201_CREATED
                }
                return Response (data_response)
            else:
                data = emp_serializer.errors
                print(data)
            return JsonResponse(data)
        except Department.DoesNotExist:
           
           return JsonResponse ({"status":status.HTTP_404_NOT_FOUND, 'message':'department does not exists'})

    def put(self, request,  *args, **kwargs):
        id_param = request.query_params.get('id', None)
        if id_param is not None:
            # If 'id' is provided, return a specific value
            try:
                instance = Employee.objects.get(id=id_param)
                print(instance)
                emp_serializer = EmployeeSerializer(instance, data=request.data, partial=True)
                if emp_serializer.is_valid():
                    emp_serializer.save()
                    return Response(emp_serializer.data)
            except Employee.DoesNotExist:
                return JsonResponse({'error': 'Not found'}, status=404)
        
    def delete(self, request,  *args, **kwargs):
        id_param = request.query_params.get('id', None)
        if id_param is not None:
            # If 'id' is provided, return a specific value
            try:
                instance = Employee.objects.get(id=id_param)
            except Employee.DoesNotExist:
                return JsonResponse({'error': 'Employee not found'}, status=404)
            instance.delete()
            return JsonResponse({"message": "Your Data has been deleted successfully", "status":True})
