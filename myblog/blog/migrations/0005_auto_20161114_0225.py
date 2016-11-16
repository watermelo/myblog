# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161107_0126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='broadside',
            options={'verbose_name': '\u4fa7\u8fb9\u680f', 'verbose_name_plural': '\u4fa7\u8fb9\u680f'},
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='\u53d1\u8868\u65f6\u95f4'),
        ),
    ]
