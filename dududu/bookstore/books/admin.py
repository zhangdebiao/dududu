#coding:utf-8
from django.contrib import admin
from books.models import Books
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'type_id', 'name', 'desc', 'price', 'unit', 'stock', 'sales', 'detail', 'image', 'status', 'publisher']


admin.site.register(Books,BooksAdmin) # 在admin中添加有关商品的编辑功能。



