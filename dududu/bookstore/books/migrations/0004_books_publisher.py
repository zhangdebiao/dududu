# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180921_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.CharField(verbose_name='商品发布者', max_length=20, default=0),
        ),
    ]
