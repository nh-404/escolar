from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('home.urls')),
    path('exam/', include('exam.urls')),
    path('classes/', include('classes.urls')),
    path('users/', include('users.urls')),
    path('student/', include('student.urls')),
    path('teacher/', include('teachers.urls')),
    path('settings/', include('escolar_settings.urls')),
    
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)