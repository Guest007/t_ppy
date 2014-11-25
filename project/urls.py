# -*- coding: utf-8 -*-
__author__ = 'guest007'
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += (static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT))
