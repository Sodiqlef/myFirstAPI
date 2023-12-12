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

class Student(models.Model):
    name = models.CharField(max_length=255)
    matric_number = models.CharField(max_length=8)
    college = models.CharField(choices=COLLEGES, max_length=50)
    department = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.matric_number