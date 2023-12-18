from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Student, School



class SchoolSerializer(ModelSerializer):
    student_count = SerializerMethodField(read_only = True)
    class Meta:
        model = School
        fields = '__all__'

    def get_student_count(self, obj):
        count = obj.school.count()
        return count

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'matric_number', 'college', 'department', 'school']


