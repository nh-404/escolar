
from django.urls import path
from . import views

urlpatterns = [

    path('', views.singIn, name='login'),
    path('signup/', views.signUp, name='signUp'),
    path('logout/', views.logout_user, name='logout'),
]
