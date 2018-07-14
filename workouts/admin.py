# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from workouts.models import Workout, TrainingSession


admin.site.register(Workout)
admin.site.register(TrainingSession)