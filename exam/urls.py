
from django.urls import path
from . import views

urlpatterns = [

    path('exam/', views.exam, name='exam'),
    path('fees/', views.fees, name='fees'),
    path('grade/', views.grade, name='grade'),
    path('result/', views.result, name='result'),
   
  
]
