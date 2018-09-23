from django.contrib import admin
from user.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id','username', 'password', 'email', 'is_login']

admin.site.register(User, UserAdmin)


