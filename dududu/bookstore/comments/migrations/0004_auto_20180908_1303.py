# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_comments_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='book',
            field=models.ForeignKey(verbose_name=b'\xe4\xb9\xa6\xe7\xb1\x8dID', to='books.Books'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.CharField(max_length=1000, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='disabled',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xa6\x81\xe7\x94\xa8\xe8\xaf\x84\xe8\xae\xba'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(default=1, verbose_name=b'\xe8\xaf\x84\xe5\x88\x86'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='title',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID', to='users.Passport'),
        ),
    ]
