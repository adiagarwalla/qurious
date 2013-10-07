# Create your views here.
from django.contrib.auth import logout
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        # logout the current user, and redirect
        # to the home screen
        logout(request)
        return HttpResponseRedirect(reverse('login'))
