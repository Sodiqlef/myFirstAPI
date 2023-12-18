from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student,School
from .serializer import StudentSerializer, SchoolSerializer

# Create your views here.

@api_view(["GET"])
def endpoints(request):
    data = ['students', 
            'student/:username',
            'schools/',
            'school/:name']
    return Response(data)


@api_view(["GET", "POST"])
def students(request):
    students = Student.objects.all()
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            pass
        else:
            students = Student.objects.filter(Q(matric_number__icontains = query) | Q(department__icontains=query))
        
        
    else: 
        student = Student.objects.create(
            name = request.data['name'],
            matric_number = request.data['matric_number'],
            college = request.data['college'],
            department = request.data['department'],
        )  
        
    serializer = StudentSerializer(students, many=True)
    data = serializer.data
    return Response(data)


@api_view(["GET", 'DELETE', 'PUT'])
def student(request, matric_number):
    try:
        student = Student.objects.get(matric_number=matric_number)
        if request.method == 'GET':
            serializer = StudentSerializer(student)
            data = serializer.data
            return Response(data)
        if request.method == 'DELETE':
            student.delete()
            return Response("User was deleted")
        if request.method == 'PUT':
            student.name = request.data['name']
            student.matric_number = request.data['matric_number']
            student.college = request.data['college']
            student.department = request.data['department']
            student.save() 
            return Response("User was updated")
    except ObjectDoesNotExist:
        return Response({'error': 'Student does not exist'}, status=404)  # 404 Not Found
   

@api_view(['GET', 'POST'])
def schools(request):
    if request.method == "GET":
        schools = School.objects.all()
        school_serializer = SchoolSerializer(schools, many=True)
        data = school_serializer.data
        return Response(data)
    if request.method == "POST":
        school = School.objects.create(
            name = request.data['name'],
            State = request.data['State'],
            ownership_type = request.data['ownership_type']

        )
        school_serializer = SchoolSerializer(school, many=False)
        data = school_serializer.data
        return Response(data)


@api_view(['GET', 'PUT'])
def school(request, name):
    try:
        school = School.objects.get(name=name)
        if request.method == "GET":
            school_serializer = SchoolSerializer(school, many=False)
            data = school_serializer.data
            return Response(data)
        if request.method == "PUT":
            updated_school = School.objects.update(
                name = request.data['name'],
                State = request.data['State'],
                ownership_type = request.data['ownership_type']
            )
            school_serializer = SchoolSerializer(school, many=False)
            data = school_serializer.data
            return Response(data)
    except ObjectDoesNotExist:
        return Response({'error': 'school not found'}, status=404)