# from django.shortcuts import render, redirect, get_object_or_404
# from teachers.models import Teacher
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# @login_required(login_url='login')
# def teacherList(request):

#     teacherDB = Teacher.objects.all()
#     teacher_count = Teacher.objects.count() 


#     return render(request, 'teacher/teacherList.html', {
#             'teacherDB': teacherDB, 
#             'teacherCount': teacher_count
#         })

# @login_required(login_url='login')
# def teacherDashboard(request):

#     return render(request, 'teacher/teacher.html')



# def add_teacher(request):


#     if request.method == 'POST':

#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         teacherID = request.POST.get('teacherId')
        
#         newTeacher = Teacher.objects.create(
#             name=name, 
#             email=email, 
#             phone=phone, 
#             age=age, 
#             gender=gender, 
#             teacherID=teacherID
#         )
        
#         newTeacher.save()
#         return redirect('teacherList')


#     return render(request, 'teacher/teacherList.html')
 


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