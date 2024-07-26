
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('', include('school_management.urls')),
    path('student', include('student.urls')),
    path('teacher', include('teacher.urls')),
    
]
