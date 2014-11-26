# -*- coding: utf-8 -*-
__author__ = 'guest007'
from .models import Post
from django.views.generic import ListView, DetailView


class PostsListView(ListView):
    model = Post
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
