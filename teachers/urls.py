from django.contrib import admin
from django.urls import path
from teachers import views

urlpatterns = [
   
     path('teacher_dashboard', views.teacher_dashboard, name='teacher_dashboard'),
     path('teacher_list', views.teacher_list, name='teacher_list'),
     path('add_teacher', views.add_teacher, name='add_teacher'),
#     path('edit/<int:id>/', views.teacher_Edit, name='teacherEdit'),  
      path('teacher_class', views.teacher_class, name='teacher_classes'),
      path('teacher_attendance', views.teacher_attendance, name='teacher_attendance'),
#      path('teacher_classes', views.t_classes, name='t_classes'),
#      path('teacher_result', views.t_result, name='t_result'),
      path('teacher_exam', views.teacher_exam, name='teacher_exam'),
      path('teacher_profile', views.teacher_profile, name='teacher_profile'),
#      path('teacher_assignment', views.t_assignment, name='t_assignment'),
#     path('remove/<int:id>/', views.teacher_Remove, name='teacherRemove'),  # Ensure <int:id> is used
]
