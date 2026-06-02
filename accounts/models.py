from django.db import models
from django.contrib.auth.models import AbstractUser

class UserTable(AbstractUser):
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    role = models.CharField(max_length=20, null=True, blank=True)

class LibrarianTable(models.Model):
    user = models.OneToOneField(
        UserTable,
        on_delete=models.CASCADE,
        related_name='librarian_profile',
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

class StudentTable(models.Model):
    user = models.OneToOneField(
        UserTable,
        on_delete=models.CASCADE,
        related_name='student_profile',
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    roll_no = models.CharField(max_length=20, null=True, blank=True)
    semester = models.CharField(max_length=20, null=True, blank=True)
# Create your models here.
