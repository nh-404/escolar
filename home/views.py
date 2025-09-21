from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from teachers.models import Teacher
from student.models import Student






@login_required(login_url='login')
def admin_dashboard(request):
    # studentDB = Student.objects.all()
    student_count = Student.objects.count() 

    # teacherDB = Teacher.objects.all()
    teacher_count = Teacher.objects.count() 

    context ={
        'student_count':student_count,
        'teacher_count':teacher_count,
    }


    return render(request, 'admin/admin_dashboard.html',context)
    
    
    #  {

    #         'studentDB': studentDB, 
    #         'count': student_count, 
    #         'teacherDB': teacherDB, 
    #         'teacherCount': teacher_count
    #     })


