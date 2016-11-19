# coding:utf-8
import logging
from collections import OrderedDict

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import (render, redirect)

from .models import (Category, Article, Broadside)
from utils.cache import cache

logger = logging.getLogger(__name__)

def index(request):
    index_articles = Article.objects.filter(published=1).order_by('-pub_date')

    limit = settings.PAGE_NUM
    paginator = Paginator(index_articles, limit)
    page = request.GET.get('page', 1)
    item_info = paginator.page(page)

    return render(request, 'index.html', {'item_info': item_info})


def category_detail(request, column_slug):
    category = Category.objects.get(slug=column_slug)
    category_articles = Article.objects.filter(
        Q(category_id=category.id) & Q(published=1)).order_by('-pub_date')

    limit = settings.PAGE_NUM
    paginator = Paginator(category_articles, limit)
    page = request.GET.get('page', 1)
    item_info = paginator.page(page)
    return render(request, 'blog/category.html',
                  {'category': category, 'item_info': item_info})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)

    if article_slug != article.slug:
        return redirect(article, permanent=True)
    # add view times
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        current_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        current_ip = request.META['REMOTE_ADDR']

    visited_ips = cache.get(article_slug, [])
    if current_ip not in visited_ips:
        article.view_times += 1
        article.save()
        visited_ips.append(current_ip)
        cache.set(article_slug, visited_ips, 5)

    return render(request, 'blog/article.html', {'article': article})


def archives(request):
    articles = Article.objects.filter(published=1).order_by('-pub_date')

    year_list = []
    archives = OrderedDict()
    # NOTE: initinal year_list, if have not article, we should give a default
    #       value.
    try:
        cur_year = articles[0].pub_date.year
        year_list.append(cur_year)
        archives[cur_year] = []
    except Exception as e:
        logger.error(u'Have no article! Error:{}'.format(e))
        return render(request, '404.html')
    for article in articles:
        cur_year = article.pub_date.year
        if cur_year not in year_list:
            year_list.append(cur_year)
            archives[cur_year] = []
        archives[cur_year].append(article)

    return render(request, 'blog/archive.html', {'archives': archives})


def resources(request):
    study_resource = Broadside.objects.filter(sign=False)
    return render(request, 'blog/resource.html', {'resources': study_resource})


def messages(request):
    return render(request, 'blog/message.html')
