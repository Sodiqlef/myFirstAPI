from django.urls import path
from . import views

urlpatterns = [
    path('endpoints/', views.endpoints),
    path('students/', views.students, name='students'),
    path('student/<str:matric_number>', views.student),
    path('schools/', views.schools, name='schools'),
    path('school/<str:name>', views.school),
] 