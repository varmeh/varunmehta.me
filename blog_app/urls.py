__author__ = 'varunmehta'

from django.conf.urls import patterns, include, url
import blog_app.views as db

urlpatterns = patterns('',
   url(r'^$', db.BlogList.as_view(), name='blog'),    #Passing string instead of callable objects
   url(r'^tag/(?P<slug>[-\w]+)/$', db.TagBlogList.as_view(), name='tags'),
   url(r'^(?P<slug>[-\w]+)/$', db.BlogDetail.as_view(), name='detail'),
)