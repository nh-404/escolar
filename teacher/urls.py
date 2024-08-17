from django.contrib import admin
from django.urls import path
from teachers import views

urlpatterns = [
   
    path('teacher', views.teacherDashboard, name='teacher'),
    path('teacherlist', views.teacherList, name='teacherList'),
    path('teacherData', views.teacherData, name='teacherData'),
    path('edit/<int:id>/', views.teacher_Edit, name='teacherEdit'),  
    path('remove/<int:id>/', views.teacher_Remove, name='teacherRemove'),  # Ensure <int:id> is used
]
