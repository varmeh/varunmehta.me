from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog_app import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.BlogList.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/$',TemplateView.as_view(template_name='about.html')),
    url(r'^blog/', include('blog_app.urls')),

    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
