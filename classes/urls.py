
from django.urls import path
from . import views

urlpatterns = [

    path('class/', views.classes, name='classes'),
    path('attendance/', views.attendance, name='attendance'),
    path('total_class/', views.total_class, name='total_class'),
   
  
]
