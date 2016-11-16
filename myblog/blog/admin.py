#!/usr/bin/env python
# coding=utf-8
from django.contrib import admin

from .models import (Category, Article, Broadside)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'create_time',
                    'update_time')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'update_time',
                    'content')


class BroadsideAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Broadside, BroadsideAdmin)
