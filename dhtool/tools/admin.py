# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import MappingTools, Inquiry, UserStories, Page
admin.site.register(MappingTools)
admin.site.register(Inquiry)
admin.site.register(UserStories)
admin.site.register(Page)
