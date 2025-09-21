from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("Admin", "Admin"),
        ("Teacher", "Teacher"),
        ("Student", "Student"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
