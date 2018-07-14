# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from profiles.models import Trainer, UserProfile


LEVEL_CHOICES = (
    (1, "Level 1"),
    (2, "Level 2"),
    (3, "Level 3")
)

class Workout(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	video_link = models.URLField(null=True, default=None)
	level = models.CharField(max_length=9,
	                  choices=LEVEL_CHOICES,
	                  default=1)

	def __str__(self):
		return self.name


class TrainingSession(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	start_date = models.DateTimeField(default=None)
	end_date = models.DateTimeField(default=None)
	trainer = models.ForeignKey(Trainer)
	users = models.ManyToManyField(UserProfile)
	workouts = models.ManyToManyField(Workout)

	def __str__(self):
		return self.name