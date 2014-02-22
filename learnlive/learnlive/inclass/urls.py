from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from learnlive.inclass import views

urlpatterns = patterns('',
        url(r'^(?P<id_tutor>\d+)/(?P<id_user>[\w\+-@.%_& ]+)/(?P<session_id>[\w\+%-_& ]+)/(?P<sign>\d+)/$', login_required(views.InClassView.as_view()), name='in-class'),
        url(r'^chat/(?P<session_id>[\w\+%-_& ]+)/(?P<message_num>\d+)/$', login_required(views.MessageChatView.as_view()), name='chat-message-get'),
        url(r'^chat/$', login_required(views.MessageChatView.as_view()), name='chat-message-post'),
        url(r'^review/$', login_required(views.ReviewPersonView.as_view()), name='review-inclass'),
        url(r'^$', login_required(views.InClassView.as_view()), name='in-class-post'),
   )
