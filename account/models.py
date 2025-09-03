from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


def generate_student_id():
    return 'STU-' + get_random_string(6).upper()


def generate_teacher_id():
    return 'TCH-' + get_random_string(6).upper()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to="students/", blank=True, null=True)

    student_id = models.CharField(max_length=20, unique=True, default=generate_student_id)

    def save(self, *args, **kwargs):
        if not self.user:
            # generate random password
            password = get_random_string(8)

            # use unique student_id as username
            username = self.student_id

            # create User
            user = User.objects.create_user(
                username=username,
                email=self.email,
                password=password
            )

            # assign Student group
            group, _ = Group.objects.get_or_create(name="Student")
            user.groups.add(group)

            self.user = user
            super().save(*args, **kwargs)

            # send email with login details
            send_mail(
                subject="Welcome to Escolar - Your Student Account",
                message=f"Hello {self.full_name},\n\n"
                        f"Your student account has been created.\n\n"
                        f"Login details:\n"
                        f"Username: {username}\n"
                        f"Password: {password}\n\n"
                        f"Please change your password after logging in.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.email],
                fail_silently=True,
            )
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to="teachers/", blank=True, null=True)

    teacher_id = models.CharField(max_length=20, unique=True, default=generate_teacher_id)

    def save(self, *args, **kwargs):
        if not self.user:
            password = get_random_string(8)

            # use unique teacher_id as username
            username = self.teacher_id

            user = User.objects.create_user(
                username=username,
                email=self.email,
                password=password
            )

            group, _ = Group.objects.get_or_create(name="Teacher")
            user.groups.add(group)

            self.user = user
            super().save(*args, **kwargs)

            send_mail(
                subject="Welcome to Escolar - Your Teacher Account",
                message=f"Hello {self.full_name},\n\n"
                        f"Your teacher account has been created.\n\n"
                        f"Login details:\n"
                        f"Username: {username}\n"
                        f"Password: {password}\n\n"
                        f"Please change your password after logging in.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.email],
                fail_silently=True,
            )
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.teacher_id})"
