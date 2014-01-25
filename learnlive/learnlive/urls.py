from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from learnlive.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from learnlive.auth.views import CreateUserView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learnlive.views.home', name='home'),
    # url(r'^learnlive/', include('learnlive.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, {'template_name': 'query_parser/LearnLive.html'}, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', CreateUserView.as_view(), name='register'),
    url(r'^inclass/$', include('learnlive.inclass.urls')),
    url(r'^', include('learnlive.query_parser.urls')),
)

urlpatterns += staticfiles_urlpatterns()
