# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=100)
    description =models.CharField(max_length=100)
    imageURL =models.CharField(max_length=100)
    passages = models.CharField(max_length=100)
    main_author = models.ForeignKey(User)
    co_authors = models.CharField(max_length=100)
    #no_iterations = models.IntegerField()
    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

    def __unicode__(self):
           return '%s %s %s' % (self.title, self.main_author,self.co_authors)

class UserExtras(models.Model):
    user_id = models.ForeignKey(User)
    gaccount = models.CharField(max_length=100)
    faccount = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    image = models.URLField()
    bookmarked = models.TextField()
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __unicode__(self):
            return '%s %s %s %s %s' % (self.gaccount, self.faccount,self.phone,self.image,self.bookmarked)


class Iterations(models.Model):
    story_id = models.ForeignKey(Story)
    it_author = models.ForeignKey(User)
    liked_by = models.TextField()
    content = models.TextField()
    class Meta:
        verbose_name = "Iteration"
        verbose_name_plural = "Iterations"

    def __unicode__(self):
            return '%s %s' % (self.liked_by, self.content)



class Comments(models.Model):
    user_id = models.ForeignKey(User)
    iteration_id = models.ForeignKey(Iterations)
    content = models.TextField()
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __unicode__(self):
            return  self.content



