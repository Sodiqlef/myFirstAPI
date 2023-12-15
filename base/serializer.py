from rest_framework.serializers import ModelSerializer

from .models import Student, School

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'