from django.shortcuts import render, redirect, get_object_or_404
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def studentList(request):
 

    return render(request, 'student/studentList.html')




def add_student(request):
    if request.method == 'POST':
        student = Student(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            dob=request.POST.get('dob') or None,
            photo=request.FILES.get('photo'),
        )
        student.save()  #
        return redirect('home')

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




def student_dashboard(request):

    return render(request, 'student/student_main.html')







@login_required(login_url='login')
def classes(request):

    return render(request, 'student/class/stu_class.html')


# @login_required(login_url='login')
# def result(request):

#     return render(request, 'result/result.html')

# @login_required(login_url='login')
# def exam(request):

#     return render(request, 'exam/exam.html')    

    

# @login_required(login_url='login')
# def student_assignment(request):

#     return render(request, 'student/student_assignment.html')   