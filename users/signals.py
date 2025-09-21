from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from student.models import Student
from teachers.models import Teacher

User = get_user_model()

@receiver(post_save, sender=Student)
def create_student_user(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create_user(
            username=f"student_{instance.roll_number}",
            password="default123",   # পরে অবশ্যই change করতে বলবে
            role="Student"
        )
        instance.user = user
        instance.save()


@receiver(post_save, sender=Teacher)
def create_teacher_user(sender, instance, created, **kwargs):
    if created and not instance.user:
        user = User.objects.create_user(
            username=f"teacher_{instance.teacher_id}",
            password="default123",   # পরে অবশ্যই change করতে বলবে
            role="Teacher"
        )
        instance.user = user
        instance.save()
