from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Student

User = get_user_model()

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ("user", "student_id", "address")
#     search_fields = ("user__username", "user__email", "student_id")

#     def save_model(self, request, obj, form, change):
#         if not obj.user:  # If no user is linked yet
#             username = f"student_{obj.student_id}"
#             email = f"{username}@example.com"

#             user = User.objects.create_user(
#                 username=username,
#                 email=email,
#                 password="default123",  # you can change later
#                 role="student"
#             )
#             obj.user = user
#         super().save_model(request, obj, form, change)

admin.site.register(Student)
