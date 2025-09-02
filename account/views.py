from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def signUp(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        newUser = User.objects.create_user(username=username, email=email, password=password)
        newUser.save()

        return render(request,'auth/login1.html',{'notify':'Account created successfully'})  


    return render(request, 'auth/signup1.html')

    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     role = request.POST['role']
    #     student_id = request.POST.get('student_id', None)

    #     user = User.objects.create_user(email=email, password=password, role=role, student_id=student_id)
    #     user.save()
    #     return redirect('login')

    # return render(request, 'auth/signup.html')



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




