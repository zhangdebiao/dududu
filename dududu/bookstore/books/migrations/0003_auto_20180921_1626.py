# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180908_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='desc',
            field=models.CharField(verbose_name='商品简介', max_length=128),
        ),
        migrations.AlterField(
            model_name='books',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='商品详情'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(verbose_name='商品图片', upload_to='books', storage=django.core.files.storage.FileSystemStorage(location='/root/桌面/django/bookstore/bookstore/static')),
        ),
        migrations.AlterField(
            model_name='books',
            name='is_delete',
            field=models.BooleanField(verbose_name='删除标记', default=False),
        ),
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(verbose_name='商品名称', max_length=20),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='books',
            name='sales',
            field=models.IntegerField(verbose_name='商品销量', default=0),
        ),
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.SmallIntegerField(verbose_name='商品状态', default=1, choices=[(0, '下线'), (1, '上线')]),
        ),
        migrations.AlterField(
            model_name='books',
            name='stock',
            field=models.IntegerField(verbose_name='商品库存', default=1),
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(verbose_name='商品种类', default=1, choices=[(1, 'IT技术'), (2, '古典名著'), (3, '课本教材'), (4, '少儿读物'), (5, '科幻小说'), (6, '鉴赏收藏')]),
        ),
        migrations.AlterField(
            model_name='books',
            name='unit',
            field=models.CharField(verbose_name='商品单位', max_length=20),
        ),
        migrations.AlterField(
            model_name='books',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
    ]
