# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161005_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadside',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u540d\u79f0')),
                ('content', django_markdown.models.MarkdownField(null=True)),
            ],
        ),
    ]
