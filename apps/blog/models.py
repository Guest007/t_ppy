# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=500, default="")
    slug = models.SlugField(_("slug"))
    short_body = models.TextField(_("Annotation"), default="")
    body = models.TextField(_("Body text"), default="")
    author = models.ForeignKey('accounts.UserProfile', related_name='author')
    image = models.CharField(upload_to="images")
    created = models.DateField(_("Creation date"), auto_now_add=True)

    class Meta:
        verbose_name = "Blog's Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        pass
