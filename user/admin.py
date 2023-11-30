from django.contrib import admin
from . models import Users

# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'password')
