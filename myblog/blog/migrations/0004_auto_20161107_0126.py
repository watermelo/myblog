# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_broadside'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadside',
            name='content',
            field=models.TextField(default=datetime.datetime(2016, 11, 7, 7, 26, 2, 246300, tzinfo=utc), max_length=500, verbose_name='\u5185\u5bb9'),
            preserve_default=False,
        ),
    ]
