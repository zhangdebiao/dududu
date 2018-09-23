#coding:utf-8
from django.contrib import admin
from users.models import *


#用户模型类
class PassportAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'username', 'password', 'email', 'is_active', 'collect']


#地址模型类
class AddressAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','recipient_name','recipient_addr','zip_code','recipient_phone','is_default','passport_id']


# Register your models here.
admin.site.register(Passport, PassportAdmin)
admin.site.register(Address, AddressAdmin)


