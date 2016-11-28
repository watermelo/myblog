#!/usr/bin/env python
# coding=utf-8
import datetime

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(u'发布日期')

    def was_published_recently(self):
        return self.pub_date


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
