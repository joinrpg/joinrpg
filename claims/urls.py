from django.conf.urls import patterns, url

from claims import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/?$', views.about),
)
