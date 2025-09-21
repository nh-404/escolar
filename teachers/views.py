# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Teacher 
from datetime import date
from student.models import Student, StudentAttendance


@login_required(login_url='login')
def teacher_list(request):

    total_teacher = Teacher.objects.all()

    context = {
        'total_teacher':total_teacher,
    }
 
    return render(request, 'teacher/teacherList.html',context)



@login_required(login_url='login')
def teacher_dashboard(request):

    return render(request, 'teacher/teacher_main.html')






User = get_user_model()

@login_required(login_url='login')
def add_teacher(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        teacher_id = request.POST.get("teacher_id").strip()
        subject = request.POST.get("subject")
        address = request.POST.get("address")
        phone = request.POST.get("phone").strip()
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        photo = request.FILES.get("photo")

        # User credentials (username + password mandatory)
        username = teacher_id.lower()   # Auto username from teacher_id
        password = phone       # Default password (change later)

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "এই Teacher ID দিয়ে account আগেই আছে।")
            return redirect("add_teacher")

        # 1) Create User
        user = User.objects.create_user(
            username=username,
            password=password,
            role="Teacher"
        )
        user.first_name = full_name
        user.email = email
        user.save()

        # 2) Create Teacher linked with User
        teacher = Teacher.objects.create(
            user=user,
            full_name=full_name,
            teacher_id=teacher_id,
            subject=subject,
            photo=photo,
            address=address,
            phone=phone,
            email=email,
            dob=dob if dob else None,
        )

        messages.success(
            request,
            f"Teacher '{full_name}' সফলভাবে যোগ হয়েছে। (username: {username}, default password: {password})"
        )
        return redirect("teacher_list")

    return render(request, "teacher/add_teacher.html")



@login_required(login_url='login')
def teacher_Edit(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':

        teacher.full_name = request.POST.get("full_name")
        teacher.subject = request.POST.get("subject")
        teacher.address = request.POST.get("address")
        teacher.phone = request.POST.get("phone").strip()
        teacher.email = request.POST.get("email")
        teacher.dob = request.POST.get("dob")
        
        if request.FILES.get("photo"):
            teacher.photo = request.FILES.get("photo")

        teacher.save()
        
        return redirect('teacher_list')  # Assuming 'index' is the name of your homepage view


    return render(request, 'teacher/edit_teacher.html', {'teacher': teacher})



@login_required(login_url='login')

def teacher_Remove(request,id):

    remove_teacher = Teacher.objects.get(id=id)
    remove_teacher.delete()
    return redirect('teacherList')   


# @login_required(login_url='login')

# def total_classes(request):


#     return render(request, 'classes/total_classes.html') 


@login_required(login_url='login')
def teacher_class(request):


    return render(request, 'teacher/teacher_class.html') 

@login_required(login_url='login')
def teacher_attendance(request):


    return render(request, 'teacher/teacher_attendance.html') 



# @login_required(login_url='login')

# def t_result(request):


    
#     return render(request, 'teacher_temp/tresult.html') 



@login_required(login_url='login')

def teacher_exam(request):


    return render(request, 'teacher/teacher_exam.html') 




@login_required(login_url='login')

def teacher_profile(request):


    return render(request, 'teacher/teacher_profile.html') 


@login_required(login_url='login')

def teacher_student_attend_list(request):

    total_student_attend = StudentAttendance.objects.all()

    context = {
        'total_student_attend':total_student_attend,
    }   



    return render(request, 'teacher/teacher_student_attend_list.html',context) 





@login_required(login_url='login')
def teacher_student_attendence(request):

    students = Student.objects.all()

    if request.method == 'POST':
         selected_date = request.POST.get("date") or date.today()

         for student in students:
            status = request.POST.get(f"attendance_{student.id}")

            if status:
                StudentAttendance.objects.update_or_create(
                    student=student,
                    date=selected_date,
                    defaults={"status": status},
                )
         return redirect('teacher_student_attend_list')


    return render(request, 'teacher/teacher_attendance.html',{
                "students": students,
                "today": date.today(),})