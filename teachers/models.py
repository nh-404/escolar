from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Teacher(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    teacher_id = models.CharField(max_length=20, unique=True)

    full_name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="teachers/", blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254, unique=True)
    dob = models.DateField(_("Date of Birth"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.user.username