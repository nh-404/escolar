from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
def login_view(request):
    
    if request.user.role == "Student":
        return redirect("student_dashboard")
    elif request.user.role == "Teacher":
        return redirect("teacher_dashboard")
    else:
        return redirect("admin_dashboard")

    return render(request, "auth/login.html")





def logout_view(request):
    logout(request)
    return redirect("login")
