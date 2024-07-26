
from django.urls import path
from school_management import views

urlpatterns = [

    path('', views.singIn, name='login'),
    path('index', views.index, name='index'),
    path('signup', views.signUp, name='signUp'),
    path('logout', views.logout_user, name='logout'),
]
