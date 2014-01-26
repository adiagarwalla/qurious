from django.conf.urls import patterns, url

from learnlive.inclass import views

urlpatterns = patterns('',
        url(r'^(?P<id_tutor>\w+)/(?P<id_user>\w+)/(?P<session_id>\w+)/(?P<sign>\w+)/$', views.InClassView.as_view(), name='in-class'),
        url(r'^$', views.InClassView.as_view(), name='in-class-post'),
   )
