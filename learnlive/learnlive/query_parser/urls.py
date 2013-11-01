from django.conf.urls import patterns, url

from learnlive.query_parser import views

urlpatterns = patterns('',
        url(r'^$', views.AskQueryView.as_view(), name='query'),
   )
