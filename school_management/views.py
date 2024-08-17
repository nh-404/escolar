from django.shortcuts import render,redirect
from student.models import Student
from teachers.models import Teacher
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




@login_required(login_url='login')
def index(request):
    studentDB = Student.objects.all()
    student_count = Student.objects.count() 

    teacherDB = Teacher.objects.all()
    teacher_count = Teacher.objects.count() 


    return render(request, 'index.html', {

            'studentDB': studentDB, 
            'count': student_count, 
            'teacherDB': teacherDB, 
            'teacherCount': teacher_count
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




def logout_user(request):

    logout(request)

    return redirect('index')

