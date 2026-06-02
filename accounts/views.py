from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserTable, LibrarianTable, StudentTable


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'librarian':
                return redirect('librarian_dashboard')
            elif user.role == 'student':
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
        
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class AdminDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != 'admin':
            return redirect('login')
        return render(request, 'accounts/admin_dashboard.html')
    
class LibrarianDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != 'librarian':
            return redirect('login')
        return render(request, 'accounts/librarian_dashboard.html')
    
class StudentDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != 'student':
            return redirect('login')
        return render(request, 'accounts/student_dashboard.html')
    
class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        if UserTable.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        user = UserTable.objects.create_user(username=username, password=password, role=role)
        user.save()
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')
