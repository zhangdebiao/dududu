from django.contrib import admin
from order.models import *


# Register your models here.
class OrderInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['order_id', 'passport_id', 'addr_id', 'total_count', 'total_price', 'transit_price', 'pay_method', 'status', 'trade_id', 'pay_method']

class OrderGoodsAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','order_id', 'books_id', 'count', 'price']


admin.site.register(OrderInfo, OrderInfoAdmin)
admin.site.register(OrderGoods, OrderGoodsAdmin)

