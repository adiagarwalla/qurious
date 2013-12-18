from django.conf.urls import patterns, url

from learnlive.query_parser import views

urlpatterns = patterns('',
        url(r'^search/$', views.AskSearchView.as_view(), name='search'),
        url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
        url(r'^results/$', views.SearchResults.as_view(), name='search-results'),
        url(r'^inclass/$', views.InClassView.as_view(), name='in-class'),
        url(r'^$', views.AskQueryView.as_view(), name='query'),
   )
