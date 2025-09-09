# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from student.models import Student
from teachers.models import Teacher



User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "student":
            Student.objects.create(user=instance)
        elif instance.role == "teacher":
            Teacher.objects.create(user=instance)
