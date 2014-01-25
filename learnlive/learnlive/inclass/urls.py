from django.conf.urls import patterns, url

from learnlive.inclass import views

urlpatterns = patterns('',
        url(r'^$', views.InClassView.as_view(), name='in-class'),
   )
