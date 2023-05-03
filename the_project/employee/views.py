# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# from .models import employee
# from .serializers import EmployeeSerializer
# from context_manager.sql_alchemy import session_scope

# import json


# @csrf_exempt
# def employee_list(request):
#     if request.method == 'GET':
#         with session_scope() as session:
#             employees = session.query(employee).all()
#             serializer = EmployeeSerializer(employees, many=True)
#             return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         serializer = EmployeeSerializer(data=data)
#         if serializer.is_valid():
#             with session_scope() as session:
#                 emp = employee(name=data['name'], age=data['age'], salary=data['salary'])
#                 session.add(emp)
#                 session.commit()
#                 return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def employee_detail(request, emp_id):
#     try:
#         with session_scope() as session:
#             emp = session.query(employee).filter_by(id=emp_id).one()
#             if request.method == 'GET':
#                 serializer = EmployeeSerializer(emp)
#                 return JsonResponse(serializer.data)

#             elif request.method == 'PUT':
#                 data = json.loads(request.body.decode('utf-8'))
#                 serializer = EmployeeSerializer(emp, data=data)
#                 if serializer.is_valid():
#                     emp.age = data['age']
#                     emp.salary = data['salary']
#                     session.commit()
#                     return JsonResponse(serializer.data)
#                 return JsonResponse(serializer.errors, status=400)

#             elif request.method == 'DELETE':
#                 session.delete(emp)
#                 session.commit()
#                 return JsonResponse({}, status=204)

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=404)

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import employee as employeeModel
from .serializers import EmployeeSerializer

@api_view(['GET'])
def employee_list(request):
    emps = employeeModel.objects.all()
    serializer = EmployeeSerializer(emps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employee_detail(request, emp_id):
    emp = get_object_or_404(employeeModel, id=id)
    serializer = EmployeeSerializer(emp)
    return Response(serializer.data)

@api_view(['POST'])
def employee_create(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def employee_update(request, id):
    emp = get_object_or_404(employeeModel, id=id)
    serializer = EmployeeSerializer(employeeModel, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def employee_delete(request, id):
    employee = get_object_or_404(employee, id=id)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
