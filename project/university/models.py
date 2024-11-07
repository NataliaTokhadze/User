from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    

class Profile(models.Model):
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
    student = models.OneToOneField('university.Student',
                                   related_name='profile',
                                   on_delete=models.CASCADE, null=True)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Profesor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    
    courses = models.ManyToManyField('university.Student',
                                   related_name='profesors')

class Class(models.Model):
    course = models.ForeignKey('university.Course',
                                   related_name='classes',
                                   on_delete=models.CASCADE, null=True)
    
    students = models.ManyToManyField('university.Student',
                                   related_name='classes',)
