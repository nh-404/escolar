
from django.contrib import admin
from django.urls import path
from student import views


urlpatterns = [

     path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
     path('student/', views.student_profile, name='student_profile'),


     path('studentt/', views.studentList, name='studentList'),
     path('add_student/', views.add_student, name='add_student'),
#     path('edit/<int:id>/', views.edit, name='edit'),  
#     path('remove/<int:id>/', views.remove, name='remove'), 
     

    path('student_timetable', views.student_timetable, name='student_timetable'),
    path('student_attendence', views.student_attendence, name='student_attendence'),

    path('student_exam', views.student_exam, name='student_exam'),
    path('student_result', views.student_result, name='student_result'),

    path('student_subects', views.student_subects, name='student_subects'),
    path('student_report', views.student_report, name='student_report'),

    path('student_fees', views.student_fees, name='student_fees'),
    path('student_libray', views.student_libray, name='student_libray'),

#     path('assignment', views.student_assignment, name='assignments'),
]
