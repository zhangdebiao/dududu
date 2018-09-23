#coding:utf-8
from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # 首页
    url(r'books/(?P<books_id>\d+)/$', views.detail, name='detail'), # 详情页
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)/$', views.list, name='list'), # 列表页
    url(r'books/add_collect/(?P<books_id>\d+)/$', views.add_collect, name='add_collect'),  # 添加收藏页
    url(r'books/borrow/(?P<books_id>\d+)/$', views.borrow, name='borrow'),  # 添加借阅页
]
