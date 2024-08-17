
from django.contrib import admin
from django.urls import path
from teacher import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher', views.teacherDashboard, name='teacher'),
    path('teacherlist', views.teacherList, name='teacherList'),
    path('teacherData', views.teacherData, name='teacherData'),
    path('edit/<int:id>/', views.teacherEdit, name='teacherEdit'),  
    path('remove/<int:id>/', views.remove, name='remove'),  # Ensure <int:id> is used
]
