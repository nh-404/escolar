from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Teacher(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    teacherID = models.CharField(max_length=10)

    def __str__(self):
        return self.name