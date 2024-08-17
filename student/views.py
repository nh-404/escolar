from django.shortcuts import render, redirect, get_object_or_404
from student.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='login')
def studentList(request):

    studentDB = Student.objects.all()
    student_count = Student.objects.count() 

    return render(request, 'studentList.html', {
            'studentDB': studentDB,
            'count': student_count
        })


@login_required(login_url='login')
def studentData(request):

    
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        studentID = request.POST.get('studentId')
        
        inserT = Student(
            name=name, 
            email=email, 
            phone=phone, 
            age=age, 
            gender=gender, 
            studentID=studentID
        )
        
        inserT.save()
        return redirect('studentList')  

    return render(request, 'studentList.html')


@login_required(login_url='login')
def edit(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.studentID = request.POST['studentId']
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.gender = request.POST['gender']
        student.phone = request.POST['phone']
        student.email = request.POST['email']
        student.save()
        return redirect('studentList')  # Assuming 'index' is the name of your homepage view

    return render(request, 'edit.html', {'student': student})



@login_required(login_url='login')

def remove(request,id):

    rm = Student.objects.get(id=id)
    rm.delete()
    return redirect('studentList')  



@login_required(login_url='login')
def studentDashboard(request):

    return render(request, 'student.html')




