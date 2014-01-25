# Create your views here.
# this Code is the property of Qurious Inc.
# Written by Abhinav Khanna

from django.views.generic import View
from django.shortcuts import render

class InClassView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/inclass.html')

    def post(self, request, *args, **kwargs):
        # This method will generate the session object corresponding to this session
        # it will then generate the notifcation to the tutor and redirect the user to
        # the proper in class page.

