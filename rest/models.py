from django.db import models

# Create your models here.
class Student(models.Model):

    student_name=models.CharField(max_length=300)
    Student_marks=models.IntegerField()
