from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required





@login_required(login_url='login')
def admin_dashboard(request):
    # studentDB = Student.objects.all()
    # student_count = Student.objects.count() 

    # teacherDB = Teacher.objects.all()
    # teacher_count = Teacher.objects.count() 


    return render(request, 'admin/admin_dashboard.html')
    
    
    #  {

    #         'studentDB': studentDB, 
    #         'count': student_count, 
    #         'teacherDB': teacherDB, 
    #         'teacherCount': teacher_count
    #     })


