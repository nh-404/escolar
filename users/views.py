from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return render(request, "auth/login.html")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            role = user.role.strip().lower() if user.role else ""

            if role == "admin":
                return redirect("admin_dashboard")
            elif role == "teacher":
                return redirect("teacher_dashboard")
            elif role == "student":
                return redirect("student_dashboard")
            else:
                messages.error(request, f"Unknown role: {user.role}")
                return redirect("login")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "auth/login.html")

    return render(request, "auth/login.html")





def logout_view(request):
    logout(request)
    return redirect("login")
