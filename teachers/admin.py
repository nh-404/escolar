from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Teacher

User = get_user_model()

@admin.register(Teacher)
class TeachertAdmin(admin.ModelAdmin):
    list_display = ("user", "teacher_id", "address")
    search_fields = ("user__username", "user__email", "teacher_id")

    def save_model(self, request, obj, form, change):
        if not obj.user:  # If no user is linked yet
            username = f"Teacher_{obj.student_id}"
            email = f"{username}@example.com"

            user = User.objects.create_user(
                username=username,
                email=email,
                password="default123",  # you can change later
                role="teacher"
            )
            obj.user = user
        super().save_model(request, obj, form, change)
