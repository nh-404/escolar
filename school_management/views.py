from django.shortcuts import render, redirect, get_object_or_404
from school_management.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    data = Student.objects.all()
    student_count = Student.objects.count() 

    return render(request, 'index.html', {
        'data': data, 'count': student_count
    })


def signUp(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        newUser = User.objects.create_user(username=username, email=email, password=password)
        newUser.save()

        return render(request,'login1.html',{'notify':'Account created successfully'})  


    return render(request, 'signup1.html')



def singIn(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
             messages.error(request, 'Invalid username or password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            login(request, user)

            return redirect('index')

        else:

            return redirect('login')

    return render(request, 'login1.html')



@login_required(login_url='login')
def insert(request):

    
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
        return redirect('index')  
        
        messages.error(request, 'Data added successfully!')        

        return render(request, 'index.html')


    return render(request, 'insert.html')


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
        return redirect('index')  # Assuming 'index' is the name of your homepage view

    return render(request, 'edit.html', {'student': student})



@login_required(login_url='login')

def remove(request,id):

        rm = Student.objects.get(id=id)
        rm.delete()


        return redirect('index')  


def logout_user(request):

    logout(request)

    return redirect('index')