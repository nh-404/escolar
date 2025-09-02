
from django.urls import path
from . import views

urlpatterns = [

    path('settings/', views.escolar_settings, name='settings'),

]
