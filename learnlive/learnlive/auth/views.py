# Create your views here.
# This code belongs to Abhinav Khanna
# Property of LearnLive Inc.
from django.contrib.auth import logout
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from learnlive.auth.models import UserProfile
from learnlive.auth.forms import UserProfileForm
from learnlive.bid_platform.models import Skill
from django.shortcuts import render

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        # logout the current user, and redirect
        # to the home screen
        logout(request)
        return HttpResponseRedirect(reverse('login'))

class CreateUserView(View):

    """
    This view will return the standard registration page
    upon get request. If a post request is made to this url
    then it will process the request object and craete a UserProfile
    object and a User object associated with it out of it.
    """

    def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        return render(request, 'auth/register_user.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # check if it is a vlid entry in the form, i.e is the form valid
        # if so, then take the values from the form and use them
        # to create a new User and UserProfile object
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # valid form entry, proceed to create the objects
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            profile_name = form.cleaned_data.get('profile_name')
            username = email

            # create the User object
            # we will leave it to the form logic to ensure that no
            # other user has this username
            user = User.objects.create_user(username, email, password)
            skill = Skill.objects.filter(name='learning')
            if len(skill) > 0:
                skill = skill[0]
            else:
                skill = Skill(name='learning')
                skill.save()

            user_profile = UserProfile(user=user, profile_name=profile_name, skills=skill)
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'auth/register_user.html', {'form': form})
