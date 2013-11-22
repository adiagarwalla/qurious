from django.conf.urls import patterns, url

from learnlive.query_parser import views

urlpatterns = patterns('',
        url(r'^search/$', views.AskSearchView.as_view(), name='search'),
        url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
        url(r'^search/results/$', views.SearchResults.as_view(), name='search-results'),
        url(r'^$', views.AskQueryView.as_view(), name='query'),
   )
