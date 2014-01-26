# Create your views here.
# this Code is the property of Qurious Inc.
# Written by Abhinav Khanna

from django.views.generic import View
from Crypto.PublicKey import RSA
from django.shortcuts import render
from learnlive.inclass.opentok_utils import generate_token

from learnlive.inclass.forms import CreateSessionForm
from learnlive.auth.models import UserProfile
from learnlive.inclass.models import Session
from learnlive.inclass.models import InClassNotification

class InClassView(View):

    def get(self, request, *args, **kwargs):
        token = generate_token("1_MX40NDU5NDk3Mn5-U2F0IEphbiAyNSAxNDozMDo1OCBQU1QgMjAxNH4wLjM3OTI0ODJ-")
        data = {
                 'token': token,
               }
        return render(request, 'query_parser/inclass.html', data)

    def generate_url(id_tutor, id_user, session_id):
        # generates the signature that will be used to create the proper url
        rsa = RSA.objects.filter()[0];
        rsa_private = RSA.importKey(rsa.private)
        (sign, random) = rsa_private.sign("" + id_tutor + "" + id_user)
        return "/" + id_tutor + "/" + id_user + "/" + sign + "/"


    def post(self, request, *args, **kwargs):
        # This method will generate the session object corresponding to this session
        # it will then generate the notifcation to the tutor and redirect the user to
        # the proper in class page.
        form = CreateSessionForm(request.POST)
        if form.is_valid():
            # we wanna create the session object here
            id_tutor = form.cleaned_data.get('id_tutor')
            id_user = form.cleaned_data.get('id_user')
            # get the UserProfile for these ids
            tutor = UserProfile.objects.get(id=id_tutor)
            user = UserProfile.objects.get(id=id_user)
            session_id = create_session('False')
            sess = Session(prof_tutor=tutor, prof_user=user, session_key=session_id)
            sess.save()
            url = self.generate_url(id_tutor, id_user, session_id)
            # generate a notification object and attach it to the tutor
            notification = InClassNotification(prof_from=user, message="Requesting a tutor session with you!", prof_to=tutor, url_inclass=url)
            notification.save()
