from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from teachers.models import Teacher, TeacherAttendance
from student.models import Student
from datetime import date





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
    


@login_required(login_url='login')
def admin_teacher_attendence_list(request):

    total_teacher_attendemce = TeacherAttendance.objects.all()

    context = {
        "total_teacher_attendemce": total_teacher_attendemce
        }


    return render(request, 'admin/admin_teacher_attendence_list.html', context)

    
    

    
@login_required(login_url='login')
def admin_teacher_attendence(request):
    

        teachers = Teacher.objects.all()

        if request.method == 'POST':
            selected_date = request.POST.get("date") or date.today()

            for teacher in teachers:
                status = request.POST.get(f"attendance_{teacher.id}")
                
                if status:
                    TeacherAttendance.objects.update_or_create(
                        teacher=teacher,
                        date=selected_date,
                        defaults={"status": status},
                    )
            return redirect('admin_teacher_attendence_list')
 

        return render(request, 'admin/admin_teacher_attendence.html',{
                "teachers": teachers,
                "today": date.today(),})
    
    

