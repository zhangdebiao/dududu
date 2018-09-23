# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20180908_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordergoods',
            options={'verbose_name': '订单商品', 'verbose_name_plural': '订单商品'},
        ),
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': '订单信息', 'verbose_name_plural': '订单信息'},
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='books',
            field=models.ForeignKey(verbose_name='订单商品', to='books.Books'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='count',
            field=models.IntegerField(verbose_name='商品数量', default=1),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='is_delete',
            field=models.BooleanField(verbose_name='删除标记', default=False),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(verbose_name='所属订单', to='order.OrderInfo'),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='price',
            field=models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='addr',
            field=models.ForeignKey(verbose_name='收货地址', to='users.Address'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='is_delete',
            field=models.BooleanField(verbose_name='删除标记', default=False),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order_id',
            field=models.CharField(verbose_name='订单编号', primary_key=True, max_length=64, serialize=False),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='passport',
            field=models.ForeignKey(verbose_name='下单账户', to='users.Passport'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_method',
            field=models.SmallIntegerField(verbose_name='支付方式', default=1, choices=[(1, '货到付款'), (2, '微信支付'), (3, '支付宝'), (4, '银联支付')]),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.SmallIntegerField(verbose_name='订单状态', default=1, choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')]),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='total_count',
            field=models.IntegerField(verbose_name='商品总数', default=1),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='total_price',
            field=models.DecimalField(verbose_name='商品总价', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='trade_id',
            field=models.CharField(verbose_name='支付编号', max_length=100, unique=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='transit_price',
            field=models.DecimalField(verbose_name='订单运费', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
    ]
