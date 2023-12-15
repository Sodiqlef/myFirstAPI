from django.db import models

# Create your models here.


COLLEGES = (
    ('Colphys', 'Colphys'),
    ('Colbios', 'Colbios'),
    ('Colerm', 'Colerm'),
    ('Coleng', 'Coleng'),
    ('Colfhec', 'Colfhec'),
    ('Colanim', 'Colanim'),
    ('Colplant', 'Colplant'),
    ('Colamrud', 'Colamrud'),
)

OWNERSHIP_TYPES = (
    ('Private', 'Private'),
    ('Federal', 'Federal'),
    ('State', 'State'),
)


class School(models.Model):
    name = models.CharField(max_length=255)
    State = models.CharField(max_length=8)
    ownership_type = models.CharField(choices=OWNERSHIP_TYPES, max_length=50)
    

    def __str__(self) -> str:
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE, related_name='school')
    matric_number = models.CharField(max_length=8)
    college = models.CharField(choices=COLLEGES, max_length=50)
    department = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.matric_number