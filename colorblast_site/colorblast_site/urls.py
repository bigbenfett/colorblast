from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'colorblast_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^colorblastapp/', include('colorblastapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
