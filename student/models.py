from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentLogin(AbstractBaseUser):

    student_ID  = models.IntegerField(max_length=10, unique=True)
    Fname       = models.CharField(max_length=200)
    Lname       = models.CharField(max_length=200)
    email       = models.EmailField(max_length=150, unique=True)
    password    = models.CharField(max_length=200)

    USERNAME_FIELD = ['']



class Student(models.Model):
    
    studentID = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name
