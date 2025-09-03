from django.contrib import admin
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from .models import Student, Teacher


def reset_student_password(modeladmin, request, queryset):
    for student in queryset:
        if student.user:
            # generate new random password
            new_password = get_random_string(8)
            student.user.set_password(new_password)
            student.user.save()

            # send email
            send_mail(
                subject="Your Escolar Student Account Password Reset",
                message=f"Hello {student.full_name},\n\n"
                        f"Your password has been reset by admin.\n\n"
                        f"Login details:\n"
                        f"Username: {student.user.username}\n"
                        f"Password: {new_password}\n\n"
                        f"Please change your password after logging in.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[student.email],
                fail_silently=True,
            )
reset_student_password.short_description = "Reset password and email students"


def reset_teacher_password(modeladmin, request, queryset):
    for teacher in queryset:
        if teacher.user:
            new_password = get_random_string(8)
            teacher.user.set_password(new_password)
            teacher.user.save()

            send_mail(
                subject="Your Escolar Teacher Account Password Reset",
                message=f"Hello {teacher.full_name},\n\n"
                        f"Your password has been reset by admin.\n\n"
                        f"Login details:\n"
                        f"Username: {teacher.user.username}\n"
                        f"Password: {new_password}\n\n"
                        f"Please change your password after logging in.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[teacher.email],
                fail_silently=True,
            )
reset_teacher_password.short_description = "Reset password and email teachers"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "student_id", "email")
    actions = [reset_student_password]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("full_name", "teacher_id", "email")
    actions = [reset_teacher_password]
