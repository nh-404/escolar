
from django.contrib import admin
from django.urls import path
from school_management import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('', views.singIn, name='login'),
    path('signup', views.signUp, name='signUp'),
    path('insert', views.insert, name='insert'),
    path('edit/<int:id>/', views.edit, name='edit'),  
    path('remove/<int:id>/', views.remove, name='remove'),  # Ensure <int:id> is used
    path('logout', views.logout_user, name='logout'),
    path('studentlist', views.studentDashboard, name='student'),
    path('student', views.studentList, name='studentList'),

]
