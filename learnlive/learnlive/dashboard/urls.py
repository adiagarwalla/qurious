from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from learnlive.dashboard import views

urlpatterns = patterns('',
        url(r'^skills/$', login_required(views.MarketableSkillView.as_view()), name='add-skill-page'),
        url(r'^skills/edit/$', login_required(views.EditSkillView.as_view()), name='edit-skill-page'),
        url(r'profile/$', login_required(views.EditProfileView.as_view()), name='edit-profile-view'),
        url(r'notifications/$', login_required(views.NotificationView.as_view()), name='notification-get'),
        url(r'^$', login_required(views.Dashboard.as_view()), name='dashboard'),
   )
