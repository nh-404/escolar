
from django.urls import path
from home import views

urlpatterns = [

    path('', views.admin_dashboard, name='admin_dashboard'),
    path('admin_teacher_attendence', views.admin_teacher_attendence, name='admin_teacher_attendence'),
    path('admin_teacher_attendence_list', views.admin_teacher_attendence_list, name='admin_teacher_attendence_list'),
   
  
]
