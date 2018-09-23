from django.contrib import admin
from comments.models import *

# Register your models here.


class CommentsAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id','disabled', 'user_id', 'book_id', 'content','title','rating']


admin.site.register(Comments, CommentsAdmin)


