# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='books',
            name='desc',
            field=models.CharField(max_length=128, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='books',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe8\xaf\xa6\xe6\x83\x85'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to=b'books', storage=django.core.files.storage.FileSystemStorage(location=b'/root/\xe6\xa1\x8c\xe9\x9d\xa2/django/bookstore/bookstore/static'), verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='books',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='books',
            name='sales',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe9\x94\x80\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')]),
        ),
        migrations.AlterField(
            model_name='books',
            name='stock',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\xba\x93\xe5\xad\x98'),
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xa7\x8d\xe7\xb1\xbb', choices=[(1, b'Python'), (2, b'Javascript'), (3, b'\xe6\x95\xb0\xe6\x8d\xae\xe7\xbb\x93\xe6\x9e\x84\xe4\xb8\x8e\xe7\xae\x97\xe6\xb3\x95'), (4, b'\xe6\x9c\xba\xe5\x99\xa8\xe5\xad\xa6\xe4\xb9\xa0'), (5, b'\xe6\x93\x8d\xe4\xbd\x9c\xe7\xb3\xbb\xe7\xbb\x9f'), (6, b'\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93')]),
        ),
        migrations.AlterField(
            model_name='books',
            name='unit',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='books',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
