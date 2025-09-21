from django.contrib import admin
from .models import Teacher, TeacherAttendance


admin.site.register(Teacher)
admin.site.register(TeacherAttendance)