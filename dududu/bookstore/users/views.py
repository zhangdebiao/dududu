#coding:utf-8
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
import re
from users.models import Passport, Address
from django.http import HttpResponse, JsonResponse
from utils.decorators import login_required
from order.models import OrderInfo, OrderGoods
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from users.tasks import send_active_email
from django.core.mail import send_mail
from django.conf import settings
import os
from django_redis import get_redis_connection
from books.models import Books
# Create your views here.



def register(request):
    '''显示用户注册页面'''
    return render(request, 'users/register.html')




def register_handle(request):
    '''进行用户注册处理'''
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    # 进行数据校验
    if not all([username, password, email]):
        # 有数据为空
        return render(request, 'users/register.html', {'errmsg':'参数不能为空!'})

    # 判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        # 邮箱不合法
        return render(request, 'users/register.html', {'errmsg':'邮箱不合法!'})

    p = Passport.objects.check_passport(username=username)

    if p:
        return render(request, 'users/register.html', {'errmsg': '用户名已存在！'})

    # 进行业务处理:注册，向账户系统中添加账户
    # Passport.objects.create(username=username, password=password, email=email)
    passport = Passport.objects.add_one_passport(username=username, password=password, email=email)

    # 生成激活的token itsdangerous
    serializer = Serializer(settings.SECRET_KEY, 3600)
    token = serializer.dumps({'confirm':passport.id}) # 返回bytes
    token = token.decode()

    # 定义邮箱发送内容
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用嘟嘟读书城。[]~(￣▽￣)~*</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的账号：</p>' \
                   '<p>http://192.168.0.104:8000/user/active/%s/</p>' % (email, token)

    # 给用户的邮箱发激活邮件
        #send_mail('嘟嘟读书城用户激活', '', settings.EMAIL_FROM, [email], \
        #  html_message='<a href="http://202.196.73.159:8000/user/active/%s/"> \
        # 亲爱的嘟嘟读用户，这是您的注册激活链接-http://202.196.73.159:8000/user/active/</a>' % token)
    send_mail('嘟嘟读书城用户激活', '', settings.EMAIL_FROM, [email], html_message=html_message)
    send_active_email.delay(token, username, email)

    # 注册完，还是返回注册页。
    return redirect(reverse('books:index'))




def login(request):
    '''显示登录页面'''
    username = ''
    checked = ''

    context = {
        'username': username,
        'checked': checked,
    }

    return render(request, 'users/login.html', context)




# /user/logout
def logout(request):
    '''用户退出登录'''
    # 清空用户的session信息
    request.session.flush()
    # 跳转到首页
    return redirect(reverse('books:index'))




def login_check(request):
    '''进行用户登录校验'''
    # 1.获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    verifycode = request.POST.get('verifycode')

    # 2.数据校验
    if not all([username, password, remember, verifycode]):
        # 有数据为空
        return JsonResponse({'res': 2})

    if verifycode.upper() != request.session['verifycode']:
        return JsonResponse({'res': 2})

    # 3.进行处理:根据用户名和密码查找账户信息
    passport = Passport.objects.get_one_passport(username=username, password=password)

    if passport:
        # 用户名密码正确
        # 获取session中的url_path
        # if request.session.has_key('url_path'):
        #     next_url = request.session.get('url_path')
        # else:
        #     next_url = reverse('books:index')
        next_url = reverse('books:index') # /user/
        jres = JsonResponse({'res': 1, 'next_url': next_url})

        # 判断是否需要记住用户名
        if remember == 'true':
            # 记住用户名
            jres.set_cookie('username', username, max_age=7*24*3600)
        else:
            # 不要记住用户名
            jres.delete_cookie('username')

        # 记住用户的登录状态
        request.session['islogin'] = True
        request.session['username'] = username
        request.session['passport_id'] = passport.id
        return jres
    else:
        # 用户名或密码错误
        return JsonResponse({'res': 0})




@login_required
def user(request):
    '''用户中心-信息页'''
    passport_id = request.session.get('passport_id')
    # 获取用户的基本信息
    addr = Address.objects.get_default_address(passport_id=passport_id)
#    addr = Address.objects.get(passport_id=passport_id)

    # 获取用户的最近浏览信息
    con = get_redis_connection('default')
    key = 'history_%d' % passport_id
    # 取出用户最近浏览的5个商品的id
    history_li = con.lrange(key, 0, 4)
    # history_li = [21,20,11]
    # print(history_li)
    # 查询数据库,获取用户最近浏览的商品信息
    # books_li = Books.objects.filter(id__in=history_li)
    books_li = []
    for id in history_li:
        books = Books.objects.get_books_by_id(books_id=id)
        books_li.append(books)

    return render(request, 'users/user_center_info.html', {'addr': addr,
                                                           'page': 'user',
                                                           'books_li': books_li})





@login_required
def address(request):
    '''用户中心-地址页'''
    # 获取登录用户的id
    passport_id = request.session.get('passport_id')

    if request.method == 'GET':
        # 显示地址页面
        # 查询用户的默认地址
        addr = Address.objects.get_default_address(passport_id=passport_id)
        return render(request, 'users/user_center_site.html', {'addr': addr, 'page': 'address'})
    else:
        # 添加收货地址
        # 1.接收数据
        recipient_name = request.POST.get('username')
        recipient_addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        recipient_phone = request.POST.get('phone')

        # 2.进行校验
        if not all([recipient_name, recipient_addr, zip_code, recipient_phone]):
            return render(request, 'users/user_center_site.html', {'errmsg': '参数不能为空!'})

        # 3.添加收货地址
        addr = Address.objects.get_default_address(passport_id=passport_id)

        if addr:
            addr.recipient_name = recipient_name
            addr.recipient_addr = recipient_addr
            addr.zip_code = zip_code
            addr.recipient_phone = recipient_phone
            addr.save()
        else:
            # 3.添加收货地址
            Address.objects.add_one_address(passport_id=passport_id,
                                            recipient_name=recipient_name,
                                            recipient_addr=recipient_addr,
                                            zip_code=zip_code,
                                            recipient_phone=recipient_phone)


        # 4.返回应答
        return redirect(reverse('user:address'))




@login_required
def order(request):
    '''用户中心-订单页'''
    # 查询用户的订单信息
    passport_id = request.session.get('passport_id')

    # 获取订单信息
    order_li = OrderInfo.objects.filter(passport_id=passport_id)

    # 遍历获取订单的商品信息
    # order->OrderInfo实例对象
    for order in order_li:
        # 根据订单id查询订单商品信息
        order_id = order.order_id
        order_books_li = OrderGoods.objects.filter(order_id=order_id)

        # 计算商品的小计
        # order_books ->OrderBooks实例对象
        for order_books in order_books_li:
            count = order_books.count
            price = order_books.price
            amount = count * price
            # 保存订单中每一个商品的小计
            order_books.amount = amount

        # 给order对象动态增加一个属性order_goods_li,保存订单中商品的信息
        order.order_books_li = order_books_li

    context = {
        'order_li': order_li,
        'page': 'order'
    }

    return render(request, 'users/user_center_order.html', context)





from django.http import HttpResponse
def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0!@#$%^&*()'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Ubuntu-RI.ttf'), 15)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')





def register_active(request, token):
    '''用户账户激活'''
    serializer = Serializer(settings.SECRET_KEY, 3600)
    try:
        info = serializer.loads(token)
        passport_id = info['confirm']
        # 进行用户激活
        passport = Passport.objects.get(id=passport_id)
        passport.is_active = True
        passport.save()
        # 跳转的登录页
        return redirect(reverse('user:login'))
    except SignatureExpired:
        # 链接过期
        return HttpResponse('激活链接已过期')







@login_required
def collect(request):
    '''用户中心-收藏页'''
    passport_id = request.session.get('passport_id')
    # 获取用户的基本信息
    username = request.session.get('username')

    user = Passport.objects.get_one_passport_by_id(username=username)

    # 如果收藏列不空
    if user.collect == '0':
        return render(request, 'users/user_center_nocollect.html', {'user': user})
    else:
        books_id = user.collect
        books = Books.objects.get_books_by_id(books_id=books_id)
        return render(request, 'users/user_center_collect.html', {'user': user,
                                                                 'books_id':books_id,
                                                                 'books': books})





@login_required
def upload(request):
    '''用户中心-上传页'''
    # 获取用户的基本信息
    passport_id = request.session.get('passport_id')

    if request.method == 'GET':
        # 显示上传页面
        #books = Books.objects.get_books_by_id(books_id=passport_id)
        return render(request, 'users/user_center_upload.html')
    else:
        # 1.接收数据
        type_id = request.POST.get('type_id')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        unit = request.POST.get('unit')
        stock = request.POST.get('stock')
        sales = request.POST.get('sales')
        detail = request.POST.get('detail')
        image = request.FILES.get('image',None)
        publisher = request.POST.get('publisher')

        # 2.进行校验
        if not all([type_id, name, desc, price, unit, stock, sales, detail, publisher]):
            return render(request, 'users/user_center_upload.html', {'errmsg': '参数不能为空!'})

        # 3.向数据库中添加图书
        Books.objects.add_one_book(type_id=type_id,
                                   name=name,
                                   desc=desc,
                                   price=price,
                                   unit=unit,
                                   stock=stock,
                                   sales=sales,
                                   detail=detail,
                                   image=image,
                                   publisher=publisher)

        # 4.返回应答
        return redirect('/')





def page_not_found(request):
    return render_to_response('404.html')

def page_error(request):
    return render_to_response('500.html')




