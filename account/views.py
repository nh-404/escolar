from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from .models import Student, Teacher

def add_student(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        photo = request.FILES.get("photo")

        # create student → this triggers auto user + ID in Student.save()
        Student.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            photo=photo,
        )
        messages.success(request, "Student account created successfully!")
        return redirect("index")  # replace with your student list page

    return render(request, "add_student.html")


def add_teacher(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        photo = request.FILES.get("photo")

        Teacher.objects.create(
            full_name=full_name,
            email=email,
            address=address,
            photo=photo,
        )
        messages.success(request, "Teacher account created successfully!")
        return redirect("classes")

    return render(request, "add_teacher.html")




# def signUp(request):

#     if request.method == 'POST':

#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         role = request.POST.get("role") 

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists')
#             return redirect('signUp')

#         user = User.objects.create(

#             username=username,
#             email=email,
#             password=make_password(password)
            
#             )

#         if role == 'student':
#             group = Group.objects.get(name='Student')
#             user.groups.add(group)

#         elif role == 'teacher':
#             group = Group.objects.get(name='Teacher')
#             user.groups.add(group)            

#         messages.success(request, f'{role.capitalize()} account create successfully')

#         return redirect('login')

#     return render(request, "auth/signup.html")








def singIn(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # # try:    
        # user = User.objects.get(username=username)
        # # except:
        # #      messages.error(request, 'Invalid username or password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            login(request, user)

            return redirect('index')

        else:

            return redirect('login')

    return render(request, 'auth/login.html')



def logout_user(request):

    logout(request)

    return redirect('index')




