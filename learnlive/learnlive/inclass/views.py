# Create your views here.
# this Code is the property of Qurious Inc.
# Written by Abhinav Khanna

from django.views.generic import View
from django.shortcuts import render
from learnlive.inclass.opentok_utils import generate_token

class InClassView(View):

    def get(self, request, *args, **kwargs):
        token = generate_token("1_MX40NDU5NDk3Mn5-U2F0IEphbiAyNSAxNDozMDo1OCBQU1QgMjAxNH4wLjM3OTI0ODJ-")
        data = {
                 'token': token,
               }
        return render(request, 'query_parser/inclass.html', data)

    def post(self, request, *args, **kwargs):
        # This method will generate the session object corresponding to this session
        # it will then generate the notifcation to the tutor and redirect the user to
        # the proper in class page.
        return
