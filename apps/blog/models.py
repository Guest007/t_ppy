# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField


class Post(models.Model):
    """
        Post model contain records for posts of blog
    """
    title = models.CharField(_("Title"), max_length=500, default="")
    slug = models.SlugField(_("slug"))
    short_body = models.TextField(_("Annotation"), default="")
    body = models.TextField(_("Body text"), default="")
    author = models.ForeignKey(User, related_name='author')
    image = ThumbnailerImageField(_('Image'), upload_to="images", blank=True)
    # image = models.ImageField(_('Image'), upload_to="images", blank=True)
    created = models.DateTimeField(_("Creation date"), auto_now_add=True)

    class Meta:
        verbose_name = "Blog's Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

