from django.conf.urls import patterns, url

from colorblastapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)