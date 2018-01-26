from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls import url, include
from django.contrib import admin
from markdownx import urls as markdownx
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



# Remember to include your view below
# example: from website.views.view_category import *
from blogpost.views.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^archive$', archive, name='archive'),
    url(r'^search_keyword/$', search_keywords, name='search_keywords'),
    url(r'^popular$', popular, name='popular'),
    url(r'^blog$', blog, name='blog'),
    url(r'^projects$', projects, name='projects'),
    url(r'^filter_blog_by_topic/(?P<topic_type>.+?)$', filter_blog_by_topic, name='filter_blog_by_topic'),
    url(r'^post/(?P<blog_id>.+?)$', get_this_post, name='get_this_post'),
    url(r'^markdownx/', include(markdownx)),
    url(r'^admin/', admin.site.urls)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





