from django.shortcuts import render, redirect, get_object_or_404
from teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def teacherList(request):

    teacherDB = Teacher.objects.all()
    teacher_count = Teacher.objects.count() 


    return render(request, 'teacherList.html', {
            'teacherDB': teacherDB, 
            'teacherCount': teacher_count
        })

@login_required(login_url='login')
def teacherDashboard(request):

    return render(request, 'teacher.html')



def teacherData(request):


    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        teacherID = request.POST.get('teacherId')
        
        newTeacher = Teacher(
            name=name, 
            email=email, 
            phone=phone, 
            age=age, 
            gender=gender, 
            teacherID=teacherID
        )
        
        newTeacher.save()
        return redirect('teacherList')


    return render(request, 'teacherList.html')
 


@login_required(login_url='login')
def teacherEdit(request, id):

    teacher = get_object_or_404(Teacher, id=id)

    if request.method == 'POST':
        teacher.teacherID = request.POST['teacherId']
        teacher.name = request.POST['name']
        teacher.age = request.POST['age']
        teacher.gender = request.POST['gender']
        teacher.phone = request.POST['phone']
        teacher.email = request.POST['email']

        teacher.save()
        
        return redirect('teacherList')  # Assuming 'index' is the name of your homepage view


    return render(request, 'teacheredit.html', {'teacher': teacher})



@login_required(login_url='login')

def remove(request,id):

    rm = Teacher.objects.get(id=id)
    rm.delete()
    return redirect('teacherList')   
