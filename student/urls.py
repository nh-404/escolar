
from django.contrib import admin
from django.urls import path
from student import views


urlpatterns = [

     path('add_student', views.add_student, name='add_student'),
#     path('edit/<int:id>/', views.edit, name='edit'),  
#     path('remove/<int:id>/', views.remove, name='remove'), 
     path('student_dashboard', views.student_dashboard, name='student_dashboard'),
      path('studentt', views.studentList, name='studentList'),
#     path('classes', views.classes, name='classes'),
#     path('result', views.result, name='result'),
#     path('exam', views.exam, name='exam'),
#     path('assignment', views.student_assignment, name='assignments'),
]
