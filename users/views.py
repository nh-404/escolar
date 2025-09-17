from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect



def login_view(request):
    
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            #  Role অনুযায়ী redirect
            if user.role == "Admin":
                return redirect("admin_dashboard")
            elif user.role == "Teacher":
                return redirect("teacher_dashboard")
            elif user.role == "Student":
                return redirect("student_dashboard")
            else:
                messages.error(request, "Unknown role for this account.")
                return redirect("login")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "auth/login.html")




def logout_view(request):
    logout(request)
    return redirect("login")
