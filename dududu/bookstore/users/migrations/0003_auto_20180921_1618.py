# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180908_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': '地址', 'verbose_name_plural': '地址'},
        ),
        migrations.AlterModelOptions(
            name='passport',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='passport',
            name='collect',
            field=models.CharField(verbose_name='用户收藏', max_length=10, default=0),
        ),
        migrations.AlterField(
            model_name='address',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_default',
            field=models.BooleanField(verbose_name='是否默认', default=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='is_delete',
            field=models.BooleanField(verbose_name='删除标记', default=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='passport',
            field=models.ForeignKey(verbose_name='账户', to='users.Passport'),
        ),
        migrations.AlterField(
            model_name='address',
            name='recipient_addr',
            field=models.CharField(verbose_name='收件地址', max_length=256),
        ),
        migrations.AlterField(
            model_name='address',
            name='recipient_name',
            field=models.CharField(verbose_name='收件人', max_length=20),
        ),
        migrations.AlterField(
            model_name='address',
            name='recipient_phone',
            field=models.CharField(verbose_name='联系电话', max_length=11),
        ),
        migrations.AlterField(
            model_name='address',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(verbose_name='邮政编码', max_length=6),
        ),
        migrations.AlterField(
            model_name='passport',
            name='create_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='email',
            field=models.EmailField(verbose_name='用户邮箱', max_length=254),
        ),
        migrations.AlterField(
            model_name='passport',
            name='is_active',
            field=models.BooleanField(verbose_name='激活状态', default=False),
        ),
        migrations.AlterField(
            model_name='passport',
            name='is_delete',
            field=models.BooleanField(verbose_name='删除标记', default=False),
        ),
        migrations.AlterField(
            model_name='passport',
            name='password',
            field=models.CharField(verbose_name='用户密码', max_length=40),
        ),
        migrations.AlterField(
            model_name='passport',
            name='update_time',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True),
        ),
        migrations.AlterField(
            model_name='passport',
            name='username',
            field=models.CharField(verbose_name='用户名称', max_length=20),
        ),
    ]
