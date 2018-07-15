# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager


class BaseUser(models.Model):
    image_url = models.URLField(null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=100, blank=True, default="")
    last_name = models.CharField(max_length=100, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserProfile(BaseUser):
	height = models.FloatField(default=0, null=True)
	weight = models.FloatField(default=0, null=True)
	age = models.IntegerField(default=0)
	location = models.CharField(max_length=200)
	bio = models.TextField()

	def __str__(self):
		return u'%s' % self.username


class Trainer(BaseUser):
	age = models.IntegerField(default=0)
	location = models.CharField(max_length=200)
	expertise = TaggableManager()

	def __str__(self):
		return u'%s' % self.username





