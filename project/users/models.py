from django.db import models
from django.contrib.auth.models import User
   
class Citizen(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    birth_date = models.DateField()
    address = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
class Passport(models.Model):
    passport_number = models.CharField(max_length=255, null=True)
    issue_date = models.DateField(auto_now_add=True)
    expire_date = models.DateField()  
    
    citizen = models.OneToOneField('users.Citizen',
                                   related_name='passport',
                                   on_delete=models.CASCADE, null=True)
    
class UserProfile(models.Model):
    user_profile = models.OneToOneField(User,
                                   related_name='userprofile',
                                   on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateField(auto_now_add=True)
    
    user_profile = models.ForeignKey('users.UserProfile',
                                    related_name='posts',
                                    on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField()
    
    citizens = models.ManyToManyField('users.Citizen',
                                      related_name='events')
    
    def __str__(self):
        return f"{self.name} event start at {self.name}"