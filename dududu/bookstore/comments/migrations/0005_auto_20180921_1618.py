# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20180908_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='book',
            field=models.ForeignKey(verbose_name='书籍ID', to='books.Books'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(verbose_name='评论内容', max_length=1000),
        ),
        migrations.AlterField(
            model_name='comments',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='disabled',
            field=models.BooleanField(verbose_name='禁用评论', default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='is_delete',
            field=models.BooleanField(verbose_name='删除标记', default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(verbose_name='评分', default=1),
        ),
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.CharField(verbose_name='评论标题', max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='comments',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(verbose_name='用户ID', to='users.Passport'),
        ),
    ]
