from django.contrib import admin
from .models import UserTable, LibrarianTable, StudentTable

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserTable

@admin.register(UserTable)
class UserTableAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {
            "fields": ("role",)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Custom Fields", {
            "fields": ("role",)
        }),
    )
admin.site.register(LibrarianTable)
admin.site.register(StudentTable)
