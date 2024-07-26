
from django.contrib import admin
from django.urls import path
from student import views


urlpatterns = [

    path('insert', views.insert, name='insert'),
    path('edit/<int:id>/', views.edit, name='edit'),  
    path('remove/<int:id>/', views.remove, name='remove'), 
    path('studentlist', views.studentDashboard, name='student'),
    path('studentt', views.studentList, name='studentList'),

]
