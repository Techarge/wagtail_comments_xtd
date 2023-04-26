from __future__ import absolute_import, unicode_literals
from wagtail_comments_xtd import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.pages, name='wagtail_comments_xtd_pages'),
    re_path(r'^(?P<pk>\d+)/$', views.comments, name='wagtail_comments_xtd_comments'),
    re_path(r'^(?P<page_pk>\d+)/comment/(?P<comment_pk>\d+)/thread/$',
        views.comment_thread, name='wagtail_comments_xtd_comment_thread'),
    re_path(r'^(?P<page_pk>\d+)/comment/(?P<comment_pk>\d+)/update/(?P<action>publish|unpublish|hide|show)/$',
        views.update, name='wagtail_comments_xtd_publication'),
]
