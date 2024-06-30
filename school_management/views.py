from django.shortcuts import render, redirect
from school_management.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginn, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):

    data = Student.objects.all()

    return render(request, 'index.html', {
        'data': data
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



def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
             messages.error(request, 'Invalid username or password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            loginn(request, user)

            return redirect('index')

        else:

            return render(request, 'login1.html')

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

        std = Student(
            name=name, 
            email=email, 
            phone=phone, 
            age=age, 
            gender=gender, 
            studentID=studentID
        )
        
        std.save()
        return redirect('index')  

        return render(request, 'index.html', {'create':'Data added successfully!'})


    return render(request, 'insert.html')


@login_required(login_url='login')
def edit(request,id):

    if request.method == 'POST':

        name =  request.POST('name')
        email = request.POST('email')
        phone = request.POST('phone')
        age =   request.POST('age')
        gender =request.POST('gender')
        studentID = request.POST('studentId')

        editData = Student.objects.get(id=id)
        editData.name
        editData.email
        editData.phone
        editData.age
        editData.gender
        editData.studentID
        editData.save()

        return redirect('index')

    log_data = Student.objects.get(id=id)
    contxt = {'log_data': log_data}

    return render(request,'edit.html', contxt)   

    return render(request, 'edit.html')



@login_required(login_url='login')
def remove(request,id):

    rm = Student.objects.get(id=id)
    rm.delete()  

    return render(request, 'remove.html')


def logout_user(request):

    logout(request)

    return redirect('index')