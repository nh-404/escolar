from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin', admin.site.urls, name='admin'),
    path('', include('school_management.urls')),
    path('student', include('student.urls')),
    path('teacher', include('teachers.urls')),
    
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)