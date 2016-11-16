#!/usr/bin/env python
# coding=utf-8
# TODO: The file is used to load data to base.html, if we use django as_viiew
#       model, we will delete this file
from .models import Category, Broadside, Article


def nav_column(request):
    nav_display_columns = Category.objects.filter(nav_display=True)
    return {'nav_display_columns': nav_display_columns}


def broadside_column(request):
    broadside_display_columns = Broadside.objects.filter(sign=True)
    return {'broadside_display_columns': broadside_display_columns}


def recent_article(request):
    # cache 10 articles
    recent_articles = Article.get_recently_article(10)
    return {'recent_articles': recent_articles}
