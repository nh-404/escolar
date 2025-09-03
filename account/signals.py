from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from . models import Student, Teacher

User = get_user_model()


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    """Ensure Student and Teacher groups exist after migration."""
    if sender.name == "account":
        Group.objects.get_or_create(name="Student")
        Group.objects.get_or_create(name="Teacher")


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Automatically create StudentProfile or TeacherProfile based on group."""
    if created:
        
        if instance.groups.filter(name="Student").exists():
            Student.objects.create(user=instance)

        elif instance.groups.filter(name="Teacher").exists():
            Teacher.objects.create(user=instance)
