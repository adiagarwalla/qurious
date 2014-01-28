from django.conf.urls import patterns, url

from learnlive.inclass import views

urlpatterns = patterns('',
        url(r'^(?P<id_tutor>\d+)/(?P<id_user>[\w\+-@.%_& ]+)/(?P<session_id>[\w\+%-_& ]+)/(?P<sign>\d+)/$', views.InClassView.as_view(), name='in-class'),
        url(r'^$', views.InClassView.as_view(), name='in-class-post'),
   )
