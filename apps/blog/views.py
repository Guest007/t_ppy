# -*- coding: utf-8 -*-
__author__ = 'guest007'
from .models import Post
from django.views.generic import ListView, DetailView


class PostsListView(ListView):
    model = Post

    def get_paginate_by(self, queryset):
        return (self.request.GET.get('per_page') or
                super(PostsListView, self).get_paginate_by(queryset))


class PostDetailView(DetailView):
    model = Post
