from django.contrib import admin
from django.urls import path
from teachers import views

urlpatterns = [
   
     path('teacher_dashboard', views.teacher_dashboard, name='teacher'),
     path('add_teacher', views.add_teacher, name='add_teacher'),
#     path('edit/<int:id>/', views.teacher_Edit, name='teacherEdit'),  
#      path('total_classes', views.total_classes, name='total_classes'),
#      path('teacher_classes', views.t_classes, name='t_classes'),
#      path('teacher_result', views.t_result, name='t_result'),
#      path('teacher_exam', views.t_exam, name='t_exam'),
#      path('teacher_assignment', views.t_assignment, name='t_assignment'),
#     path('remove/<int:id>/', views.teacher_Remove, name='teacherRemove'),  # Ensure <int:id> is used
]
