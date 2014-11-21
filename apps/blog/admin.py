# -*- coding: utf-8 -*-
__author__ = 'guest007'
from django.conf import settings
import datetime
from django.contrib import admin
from .models import Post


class BlogAdmin(admin.ModelAdmin):

    model = Post

    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'author', 'created')
    search_fields = ('title', )

admin.site.register(Post, BlogAdmin)

