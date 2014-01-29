# Create your views here.
# this Code is the property of Qurious Inc.
# Written by Abhinav Khanna

from django.views.generic import View
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.shortcuts import redirect
from Crypto.PublicKey import RSA
from learnlive.inclass.models import RSA as RSA_O
from django.shortcuts import render
from learnlive.inclass.opentok_utils import generate_token
from learnlive.inclass.opentok_utils import create_session
from learnlive.inclass.opentok_utils import API_KEY

from learnlive.inclass.forms import CreateSessionForm
from learnlive.auth.models import UserProfile
from learnlive.inclass.models import Session
from learnlive.inclass.models import InClassNotification

class InClassView(View):

    def get(self, request, *args, **kwargs):
        id_tutor = self.kwargs['id_tutor']
        username = self.kwargs['id_user']
        sign = self.kwargs['sign']
        session_id = self.kwargs['session_id']
        rsa = RSA_O.objects.filter()[0]
        rsa_public = RSA.importKey(rsa.public)
        user = User.objects.get(username=username)
        message = int(id_tutor) + int(user.id)
        message_num = int(message)
        if not rsa_public.verify(message_num, (int(sign), 16)):
            return redirect('/')

        # proceed to ensure that it is still a valid session
        sess = Session.objects.get(session_key=session_id)
        if sess.is_cancelled == True:
            return redirect('/')

        token = generate_token(session_id)
        data = {
                 'token': token,
                 'session_id': session_id,
                 'api_key': API_KEY,
               }
        return render(request, 'query_parser/inclass.html', data)

    def generate_url(self, id_tutor, id_user, session_id):
        # generates the signature that will be used to create the proper url
        rsa = RSA_O.objects.filter()[0];
        rsa_private = RSA.importKey(rsa.private)
        user = User.objects.get(username=id_user)
        message = int(id_tutor) + int(user.id) 
        message_num = int(message)
        sign_tuple = rsa_private.sign(message_num, 16)
        sign = sign_tuple[0]
        return '/inclass/' + str(id_tutor) + '/' + str(id_user) + '/' + str(session_id) + '/' + str(sign) + '/'


    def post(self, request, *args, **kwargs):
        # This method will generate the session object corresponding to this session
        # it will then generate the notifcation to the tutor and redirect the user to
        # the proper in class page.
        form = CreateSessionForm(request.user, request.POST)
        if form.is_valid():
            # we wanna create the session object here
            id_tutor = form.cleaned_data.get('id_tutor')
            username = form.cleaned_data.get('id_user')
            # get the UserProfile for these ids
            tutor = UserProfile.objects.get(id=id_tutor)
            user_O = User.objects.get(username=username)
            user = UserProfile.objects.get(user=user_O)
            session_id = create_session('True')
            sess = Session(prof_tutor=tutor, prof_user=user, session_key=session_id, time=15)
            sess.save()
            url = self.generate_url(id_tutor, username, session_id)
            # generate a notification object and attach it to the tutor
            notification = InClassNotification(prof_from=user, m_type=1,  message='Requesting a tutor session with you!', prof_to=tutor, url_inclass=url)
            notification.save()
            return redirect(url)
        else:
            return redirect('/')

class MessageChatView(View):
    """
    This is the view that acts as an endpoint for the chat service that we are establishing
    """

    def get(self, request, *args, **kwargs):
        session_id = self.kwargs['session_id']
        message_num = self.kwargs['message_num']
        # the messages after message_num

        messages = []
        sess = Session.objects.get(session_key=session_id)
        for message in sess.message_set.all():
            if message.seq_number > message_num:
                messages.append(message)

        data = simplejson.dumps({'messages': messages})
        return HttpResponse(data, mimetype='application/json')

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            session_id = form.cleaned_data.get('session_id')
            sess = Session.objects.get(session_key=session_id)
            username = request.user.username
            user = User(username=username)
            seq_number = sess.message_set.all()[-1]
            m = Message(content=content, 

        data = simplejson.dumps({})
        return HttpResponse(data, mimetype='application/json')

