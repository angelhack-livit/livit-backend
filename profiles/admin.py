# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from profiles.models import UserProfile, Trainer

admin.site.register(UserProfile)
admin.site.register(Trainer)