# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Teacher 



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
        return redirect("add_teacher")

    return render(request, "teacher/add_teacher.html")

# def add_teacher(request):


#     if request.method == 'POST':

#         teacher = Teacher.objects.create(

#             subject    =request.POST.get('subject'),
#             teacher_id =   request.POST.get('teacher_id'),
#             full_name = request.POST.get('full_name'),
#             email = request.POST.get('email'),
#             phone = request.POST.get('phone'),
#             address = request.POST.get('address'),
#             dob = request.POST.get('dob'),
#             photo = request.FILES.get('photo'),
#         )
#         teacher.save()
        
#         return redirect('home')


#     return render(request, 'teacher/teacher_add.html')
 


# @login_required(login_url='login')
# def teacher_Edit(request, id):

#     teacher = get_object_or_404(Teacher, id=id)

#     if request.method == 'POST':
#         teacher.teacherID = request.POST['teacherId']
#         teacher.name = request.POST['name']
#         teacher.age = request.POST['age']
#         teacher.gender = request.POST['gender']
#         teacher.phone = request.POST['phone']
#         teacher.email = request.POST['email']

#         teacher.save()
        
#         return redirect('teacherList')  # Assuming 'index' is the name of your homepage view


#     return render(request, 'teacher/teacheredit.html', {'teacher': teacher})



# @login_required(login_url='login')

# def teacher_Remove(request,id):

#     teacherRm = Teacher.objects.get(id=id)
#     teacherRm.delete()
#     return redirect('teacherList')   


# @login_required(login_url='login')

# def total_classes(request):


#     return render(request, 'classes/total_classes.html') 


# @login_required(login_url='login')

# def t_classes(request):


#     return render(request, 'teacher_temp/tclass.html') 



# @login_required(login_url='login')

# def t_result(request):


    
#     return render(request, 'teacher_temp/tresult.html') 



# @login_required(login_url='login')

# def t_exam(request):



#     return render(request, 'teacher_temp/texam.html') 



# @login_required(login_url='login')

# def t_assignment(request):

#     return render(request, 'teacher_temp/tassignment.html') 