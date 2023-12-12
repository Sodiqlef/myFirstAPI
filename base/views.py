from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializer import StudentSerializer

# Create your views here.

@api_view(["GET"])
def endpoints(request):
    data = ['students', 'student/:username']
    return Response(data)


@api_view(["GET"])
def students(request):
    students = Student.objects.all()
    query = request.GET.get('query')
    if query == None:
        pass
    else:
        students = Student.objects.filter(Q(matric_number__icontains = query) | Q(department__icontains=query))
    
    serializer = StudentSerializer(students, many=True)
    data = serializer.data
    return Response(data)


@api_view(["GET"])
def student(request, matric_number):
    student = Student.objects.get(matric_number=matric_number)
    serializer = StudentSerializer(student)
    data = serializer.data
    return JsonResponse(data, safe=False)