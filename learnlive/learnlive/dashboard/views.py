# Create your views here.
# This is the view code for the main dashboard segment
# Author: Abhinav Khanna

from django.views.generic import View
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.core import serializers
from django.shortcuts import render
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

from learnlive.bid_platform.models import Skill
from learnlive.inclass.models import InClassNotification

from learnlive.dashboard.forms import AddSkillForm
from learnlive.dashboard.forms import EditSkillForm
from learnlive.dashboard.forms import EditProfileForm
from learnlive.dashboard.forms import NotificationUpdateForm

class MarketableSkillView(View):
    """
    This is the view for the marketable skills page
    This view should allow you to get all possible
    skills belonging to this user, and color code
    them based on marketablility
    """

    def get(self, request, *args, **kwargs):
        # return the list of skills for the logged in user
        # assumes that hte person is logged in.
        username = request.user.username
        user = User.objects.get(username=username)
        user_prof = user.userprofile
        skills = user_prof.skills.all()

        data = serializers.serialize('json', skills)
        return HttpResponse(data, mimetype='application/json')

    def post(self, request, *args, **kwargs):
        # allows you to post a new skill to your profile
        lmtzr = WordNetLemmatizer()
        form = AddSkillForm(request.POST)
        if form.is_valid():
            skill_name = form.cleaned_data.get('new_skill')
            skill_lemma = lmtzr.lemmatize(skill_name)
            username = request.user.username
            user = User.objects.get(username=username)
            user_prof = user.userprofile
            skill = Skill(name=skill_name, is_marketable=False, num_endorsements=0, price=0, lemma_name=skill_lemma)
            skill.save()
            user_prof.skills.add(skill)

        data = simplejson.dumps({})
        return HttpResponse(data, mimetype='application/json')


class EditSkillView(View):

    def post(self, request, *args, **kwargs):
        """
        Allows you to modify an existing skill that you have, maybe to make it marketable and add a price
        """
        form = EditSkillForm(request.POST)
        if form.is_valid():
            skill = Skill.objects.get(id=form.cleaned_data.get('skill_id'))
            price = form.cleaned_data.get('price')
            marketable = form.cleaned_data.get('is_marketable')
            desc = form.cleaned_data.get('desc')
            if marketable == 0:
                skill.is_marketable = False
            else:
                skill.is_marketable = True
            skill.price = price
            skill.desc = desc
            skill.save()

        data = simplejson.dumps({})
        return HttpResponse(data, mimetype='application/json')


class EditProfileView(View):
    """
    This ivew edits the profile, allowing you to update it with stuff.
    """
    def post(self, request, *args, **kwargs):
        form = EditProfileForm(request.POST)
        if form.is_valid():
            username = request.user.username
            user = User.objects.get(username=username)
            user_prof = user.userprofile
            user_prof.profile_name = form.cleaned_data.get('profile_name')
            user_prof.bio = form.cleaned_data.get('bio')
            user_prof.save()

        data = simplejson.dumps({})
        return HttpResponse(data, mimetype='application/json')

    def get(self, request, *args, **kwargs):
        """
        Gets the basic profile for the user currently logged in
        """
        username = request.user.username
        user = User.objects.get(username=username)
        user_prof = user.userprofile

        data = serializers.serialize('json', [user_prof])
        return HttpResponse(data, mimetype='application/json')


class NotificationView(View):

    def get(self, request, *args, **kwargs):
        """
        This view will return the notification objects back to the end user.
        """
        username = request.user.username
        user = User.objects.get(username=username)
        user_prof = user.userprofile
        notifications = user_prof.id_to.all()

        data = serializers.serialize('json', notifications)
        return HttpResponse(data, mimetype='application/json')

    def post(self, request, *args, **kwargs):
        """
        This is what allows a notification to be marked as read
        """
        form = NotificationUpdateForm(request.POST)
        if form.is_valid():
            notification_url = form.cleaned_data.get('notification_url')
            notification = InClassNotification.objects.get(url_inclass=notification_url)
            notification.delete()

        data = simplejson.dumps({})
        return HttpResponse(data, mimetype='application/json')

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/dashboard.html')

