from django.shortcuts import render, redirect, get_object_or_404
from student.models import Student
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='login')
def student_dashboard(request):

    return render(request, 'student/student_main.html')



@login_required(login_url='login')
def student_profile(request):

    return render(request, 'student/student_profile.html')



@login_required(login_url='login')
def studentList(request):

    total_student = Student.objects.all()

    context = {
        'total_student':total_student,
    }
 
    return render(request, 'student/studentList.html',context)



User = get_user_model()

@login_required(login_url='login')
def add_student(request):

    if request.method == 'POST':

        full_name = request.POST.get("full_name")
        roll_number = request.POST.get("student_id").strip()
        class_name = request.POST.get("student_class")
        address = request.POST.get("address")
        phone = request.POST.get("phone").strip()
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        photo = request.FILES.get("photo")


        username = roll_number.lower()
        password = phone

        if User.objects.filter(username=username).exists():
            messages.error(request, "এই Student ID দিয়ে account আগেই আছে।")
            return redirect("add_student")

        user= User.objects.create_user(
            username=username, 
            password=password,
            role='Student'
            )
        user.first_name=full_name
        user.email=email
        user.save()

        student = Student.objects.create(            
            user=user,
            full_name=full_name,
            roll_number=roll_number,
            class_name=class_name,
            photo=photo,
            address=address,
            phone=phone,
            email=email,
            dob=dob if dob else None,)

         
        return redirect('add_student')

    return render(request, 'student/student_add.html')


# @login_required(login_url='login')
# def edit(request, id):

#     student = get_object_or_404(Student, id=id)

#     if request.method == 'POST':
#         student.studentID = request.POST['studentId']
#         student.name = request.POST['name']
#         student.age = request.POST['age']
#         student.gender = request.POST['gender']
#         student.phone = request.POST['phone']
#         student.email = request.POST['email']
#         student.save()
#         return redirect('studentList')  # Assuming 'index' is the name of your homepage view

#     return render(request, 'base/edit.html', {'student': student})



# @login_required(login_url='login')

# def remove(request,id):

#     rm = Student.objects.get(id=id)
#     rm.delete()
#     return redirect('studentList')  





@login_required(login_url='login')
def student_attendence(request):

    return render(request, 'student/student_attendence.html')



@login_required(login_url='login')
def student_timetable(request):

    return render(request, 'student/student_timetable.html')



@login_required(login_url='login')
def student_exam(request):

    return render(request, 'student/exam/student_exam.html')



@login_required(login_url='login')
def student_report(request):

    return render(request, 'student/student_report.html')



@login_required(login_url='login')
def student_fees(request):

    return render(request, 'student/student_fees.html')



@login_required(login_url='login')
def student_libray(request):

    return render(request, 'student/student_libray.html')




def student_subects(request):

    return render(request, 'student/student_subects.html')



@login_required(login_url='login')
def student_class(request):

    return render(request, 'student/class/student_class.html')



@login_required(login_url='login')
def student_result(request):

    return render(request, 'student/result/student_result.html')



# @login_required(login_url='login')
# def exam(request):

#     return render(request, 'exam/exam.html')    

    

# @login_required(login_url='login')
# def student_assignment(request):

#     return render(request, 'student/student_assignment.html')   