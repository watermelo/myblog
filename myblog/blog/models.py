# coding:utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django_markdown.models import MarkdownField
from utils.cache import cache_decorator


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField("名称", max_length=40)
    slug = models.CharField("别名", max_length=40)
    intro = models.TextField("简介", default='')

    nav_display = models.BooleanField('导航显示', default=False)
    home_display = models.BooleanField('首页显示', default=False)

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/%s/' % ('category', self.slug)

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'
        ordering = ['name']


@python_2_unicode_compatible
class Article(models.Model):
    category = models.ForeignKey(Category, verbose_name='归属类别')

    title = models.CharField("标题", max_length=40)
    slug = models.CharField("别名", max_length=40)

    pub_date = models.DateTimeField('发表时间', auto_now_add=False, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    author = models.ForeignKey('auth.User', blank=True,
                               null=True, verbose_name='作者')
    content = MarkdownField(null=True)

    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/%s/' % ('article', self.pk, self.slug)

    @classmethod
    @cache_decorator(1*60)
    def get_recently_article(cls, num):
        return cls.objects.filter(published=1).order_by('-pub_date')[:num]

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-pub_date']


@python_2_unicode_compatible
class Broadside(models.Model):
    # TODO: the broadside model include sidebar and static resource. need to
    # take out one of them.
    name = models.CharField("名称", max_length=40)
    content = models.TextField('内容', max_length=500)
    sign = models.BooleanField('资源标识')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '侧边栏'
        verbose_name_plural = '侧边栏'
