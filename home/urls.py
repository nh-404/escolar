
from django.urls import path
from home import views

urlpatterns = [

    path('', views.admin_dashboard, name='admin_dashboard'),
   
  
]
