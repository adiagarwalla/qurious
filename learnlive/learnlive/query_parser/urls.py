from django.conf.urls import patterns, url

from learnlive.query_parser import views

urlpatterns = patterns('',
        url(r'^$', views.AskSearchView.as_view(), name='search'),
        url(r'^v2/$', views.AlternateSearchView.as_view(), name='alt'),
        url(r'^search/$', views.ProcessSearchView.as_view(), name='process-search'),
        url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
        url(r'^results/$', views.SearchResults.as_view(), name='search-results'),
        url(r'^aboutus/$', views.AboutUs.as_view(), name='about-us'),
        url(r'^confirmation/$', views.Confirm.as_view(), name='confirm'),               
   )
