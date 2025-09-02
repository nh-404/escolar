from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from student.models import Student
from teachers.models import Teacher




@login_required(login_url='login')
def home(request):
    studentDB = Student.objects.all()
    student_count = Student.objects.count() 

    teacherDB = Teacher.objects.all()
    teacher_count = Teacher.objects.count() 


    return render(request, 'base/index.html', {

            'studentDB': studentDB, 
            'count': student_count, 
            'teacherDB': teacherDB, 
            'teacherCount': teacher_count
        })


