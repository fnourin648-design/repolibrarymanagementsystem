from django.urls import path
from . import views
from .views import LoginView, LogoutView, AdminDashboardView, LibrarianDashboardView, StudentDashboardView, RegisterView

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin_dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('librarian_dashboard/', views.LibrarianDashboardView.as_view(), name='librarian_dashboard'),
    path('student_dashboard/', views.StudentDashboardView.as_view(), name='student_dashboard'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
