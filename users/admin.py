from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from student.models import Student
from teachers.models import Teacher
from .models import User

class CustomUserAdmin(UserAdmin):
    # Show role in admin list
    list_display = ("username", "email", "first_name", "last_name", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Role & Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "role", "password1", "password2", "is_staff", "is_active")}
        ),
    )

    search_fields = ("username", "email")
    ordering = ("username",)

admin.site.register(User, CustomUserAdmin)



User = get_user_model()

# --- Inline for Student ---
class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    extra = 0

# --- Inline for Teacher ---
class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False
    extra = 0

