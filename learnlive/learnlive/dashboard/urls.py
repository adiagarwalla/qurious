from django.conf.urls import patterns, url

from learnlive.dashboard import views

urlpatterns = patterns('',
        url(r'^skills/$', views.MarketableSkillView.as_view(), name='add-skill-page'),
        url(r'^skills/edit/$', views.EditSkillView.as_view(), name='edit-skill-page'),
        url(r'profile/$', views.EditProfileView.as_view(), name='edit-profile-view'),
        url(r'^$', views.Dashboard.as_view(), name='dashboard'),
   )
