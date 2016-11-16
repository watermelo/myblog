# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161114_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='broadside',
            name='sign',
            field=models.BooleanField(default=datetime.datetime(2016, 11, 14, 15, 57, 2, 700158, tzinfo=utc), verbose_name='\u8d44\u6e90\u6807\u8bc6'),
            preserve_default=False,
        ),
    ]
