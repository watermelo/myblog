# coding:utf-8
from collections import OrderedDict

from django.shortcuts import (render, redirect)
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import (Category, Article, Broadside)


def index(request):
    index_articles = Article.objects.filter(published=1).order_by('-pub_date')

    # NOTE: Restrictions per article in one page
    limit = 5
    paginator = Paginator(index_articles, limit)
    page = request.GET.get('page', 1)
    item_info = paginator.page(page)

    return render(request, 'index.html', {'item_info': item_info})


def category_detail(request, column_slug):
    category = Category.objects.get(slug=column_slug)
    category_articles = Article.objects.filter(published=1).\
        filter(category_id=category.id).order_by('-pub_date')
    limit = 5
    paginator = Paginator(category_articles, limit)
    page = request.GET.get('page', 1)
    item_info = paginator.page(page)
    return render(request, 'blog/category.html',
                  {'category': category, 'item_info': item_info})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)

    if article_slug != article.slug:
        return redirect(article, permanent=True)

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
    except Exception:
        print "Have no article!"
        return
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
