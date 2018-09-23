#coding:utf-8
from django.shortcuts import render, redirect
from books.models import Books
from users.models import Passport, Address
from comments.models import Comments
from comments.models import *
from books.enums import *
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection
import random
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
import logging
logger = logging.getLogger('django.request')
# @cache_page(60 * 15)




def index(request):
    '''显示首页'''
    # 查询每个种类的3个新品信息和4个销量最好的商品信息
    python_new = Books.objects.get_books_by_type(PYTHON, 3, sort='new')
    python_hot = Books.objects.get_books_by_type(PYTHON, 4, sort='hot')
    javascript_new = Books.objects.get_books_by_type(JAVASCRIPT, 3, sort='new')
    javascript_hot = Books.objects.get_books_by_type(JAVASCRIPT, 4, sort='hot')
    algorithms_new = Books.objects.get_books_by_type(ALGORITHMS, 3, sort='new')
    algorithms_hot = Books.objects.get_books_by_type(ALGORITHMS, 4, sort='hot')
    machinelearning_new = Books.objects.get_books_by_type(MACHINELEARNING, 3, sort='new')
    machinelearning_hot = Books.objects.get_books_by_type(MACHINELEARNING, 4, sort='hot')
    operatingsystem_new = Books.objects.get_books_by_type(OPERATINGSYSTEM, 3, sort='new')
    operatingsystem_hot = Books.objects.get_books_by_type(OPERATINGSYSTEM, 4, sort='hot')
    database_new = Books.objects.get_books_by_type(DATABASE, 3, sort='new')
    database_hot = Books.objects.get_books_by_type(DATABASE, 4, sort='hot')

    # 随机生成书海
    ran = random.randint(8,33)

    # 定义模板上下文
    context = {
        'python_new': python_new,
        'python_hot': python_hot,
        'javascript_new': javascript_new,
        'javascript_hot': javascript_hot,
        'algorithms_new': algorithms_new,
        'algorithms_hot': algorithms_hot,
        'machinelearning_new': machinelearning_new,
        'machinelearning_hot': machinelearning_hot,
        'operatingsystem_new': operatingsystem_new,
        'operatingsystem_hot': operatingsystem_hot,
        'database_new': database_new,
        'database_hot': database_hot,
        'ran':ran,
    }

    # 使用模板
    if request.session.has_key('username'):
        logger.info(request.session["username"])
    else:
        logger.info('anonymous')
    return render(request, 'books/index.html', context)




def detail(request, books_id):
    '''显示商品的详情页面'''
    # 获取商品的详情信息
    books = Books.objects.get_books_by_id(books_id=books_id)

    if books is None:
        # 商品不存在，跳转到首页
        return redirect(reverse('books:index'))

    # 新品推荐
    books_li = Books.objects.get_books_by_type(type_id=books.type_id, limit=2, sort='new')

    # 用户登录之后，才记录浏览记录
    # 每个用户浏览记录对应redis中的一条信息 格式:'history_用户id':[10,9,2,3,4]
    # [9, 10, 2, 3, 4]
    if request.session.has_key('islogin'):
        # 用户已登录，记录浏览记录
        con = get_redis_connection('default')
        key = 'history_%d' % request.session.get('passport_id')
        # 先从redis列表中移除books.id
        con.lrem(key, 0, books.id)
        con.lpush(key, books.id)
        # 保存用户最近浏览的5个商品
        con.ltrim(key, 0, 4)

    ran = random.randint(8,33)

    # 评论查询
    comm_li = Comments.objects.get_comms_by_bookid(book_id=books_id, limit=10, sort='new')

    # 定义上下文
    context = {'books': books, 'books_li': books_li, 'ran':ran, 'comm_li':comm_li}

    # 使用模板
    return render(request, 'books/detail.html', context)




# 商品种类 页码 排序方式
# /list/(种类id)/(页码)/?sort=排序方式
def list(request, type_id, page):
    '''商品列表页面'''
    # 获取排序方式
    sort = request.GET.get('sort', 'default')

    # 判断type_id是否合法
    if int(type_id) not in BOOKS_TYPE.keys():
        return redirect(reverse('books:index'))

    # 根据商品种类id和排序方式查询数据
    books_li = Books.objects.get_books_by_type(type_id=type_id, sort=sort)

    # 分页
    paginator = Paginator(books_li, 1)

    # 获取分页之后的总页数
    num_pages = paginator.num_pages

    # 取第page页数据
    if page == '' or int(page) > num_pages:
        page = 1
    else:
        page = int(page)

    # 返回值是一个Page类的实例对象
    books_li = paginator.page(page)

    # 进行页码控制
    # 1.总页数<5, 显示所有页码
    # 2.当前页是前3页，显示1-5页
    # 3.当前页是后3页，显示后5页 10 9 8 7
    # 4.其他情况，显示当前页前2页，后2页，当前页
    if num_pages < 5:
        pages = range(1, num_pages+1)
    elif page <= 3:
        pages = range(1, 6)
    elif num_pages - page <= 2:
        pages = range(num_pages-4, num_pages+1)
    else:
        pages = range(page-2, page+3)

    # 新品推荐
    books_new = Books.objects.get_books_by_type(type_id=type_id, limit=2, sort='new')

    # 随机生成书海
    ran = random.randint(8,33)

    # 定义上下文
    type_title = BOOKS_TYPE[int(type_id)]
    context = {
        'books_li': books_li,
        'books_new': books_new,
        'type_id': type_id,
        'sort': sort,
        'type_title': type_title,
        'pages': pages,
        'ran':ran
    }

    # 使用模板
    return render(request, 'books/list.html', context)




def add_collect(request, books_id):
    '''添加收藏'''
    books = Books.objects.get_books_by_id(books_id=books_id)

    if books is None:
        # 商品不存在，跳转到首页
        return redirect(reverse('books:index'))

    # 获取用户的基本信息
    username = request.session.get('username')
    user = Passport.objects.get_one_passport_by_id(username=username)

    user.collect = books_id
    user.save()

    return redirect('/books/%s' % books_id)




def rand_str():
    room_id = ""
    for i in range(10):
        alpha = chr(random.randint(65, 90))  # random.randrange(65,91)
        alpha_lower = chr(random.randint(97, 122))  # random.randrange(65.91)
        num = str(random.randint(0, 9))
        ret = random.choice([alpha, num, alpha_lower])
        room_id += ret
    return  room_id




def borrow(request, books_id):
    '''借阅页面'''
    username = request.session.get('username')
    user = Passport.objects.get_one_passport_by_id(username=username)

    # 通过id获取type_id
    books = Books.objects.get_books_by_id(books_id=books_id)
    type_id = books.type_id

    # 获取商品发布者邮箱
    publisher = books.publisher
    user_publisher = Passport.objects.get_one_passport_by_id(username=publisher)
    email = user_publisher.email

    # 获取排序方式
    sort = request.GET.get('sort', 'default')

    # 判断type_id是否合法
    if int(type_id) not in BOOKS_TYPE.keys():
        return redirect(reverse('books:index'))

    # 根据商品种类id和排序方式查询数据
    books_li = Books.objects.get_books_by_type(type_id=type_id, sort=sort)

    # 新品推荐
    books_new = Books.objects.get_books_by_type(type_id=type_id, limit=2, sort='new')

    # 随机生成书海
    ran = random.randint(8,33)

    # 随机生成房间号
    room_id = rand_str()

    # 定义邮箱发送内容
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用嘟嘟读书城。[]~(￣▽￣)~*</p>' \
                   '<p>嘟嘟读用户:<b>%s</b> 想要借阅您在嘟嘟读书城发布的:<b>《%s》</b><p>' \
                   '<p>系统为您生成的实时聊天系统房间号为：<b>%s</b></p>' \
                   '<p>请您登录<a href="http://192.168.0.101:8000/" target="_blank">嘟嘟读-实时聊天系统。</a></p>' % (user.username, books.name, room_id)

    # 给用户的邮箱发系统房间号邮件
    send_mail('嘟嘟读书城用户图书借阅通知', '', settings.EMAIL_FROM, [email], html_message=html_message)


    # 定义上下文
    type_title = BOOKS_TYPE[int(type_id)]
    context = {
        'book': books,
        'books_new': books_new,
        'type_id': type_id,
        'type_title': type_title,
        'ran':ran,
        'room_id':room_id,
    }

    return render(request, 'books/borrow.html', context)






