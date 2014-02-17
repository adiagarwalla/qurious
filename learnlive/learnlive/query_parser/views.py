# Create your views here.
# This code is the property of Learnlive Inc
# Written by Abhinav Khanna

from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect
from warnings import warn
from learnlive.inclass.opentok_utils import create_session, generate_token
from learnlive.query_parser.query_utils import get_category_for_verb
from learnlive.query_parser.query_utils import get_entity_list
from learnlive.bid_platform.skill_utils import get_profile_for_entity

from learnlive.query_parser.forms import QueryRequestForm
from learnlive.query_parser.forms import LeaveMessageForm
from learnlive.query_parser.models import LeaveMessage

from learnlive.query_parser.query_utils import tokenize_query, get_NE, get_skills

class AskQueryView(View):
    """
    This is the view for the main landing page
    where a query can be inserted. I.E the home landing
    page that looks like google's.
    """

    def get(self, request, *args, **kwargs):
        warn('You are hitting a testing page')
        form = QueryRequestForm()
        return render(request, 'query_parser/query.html', {'form': form})

    def post(self, request, *args, **kwargs):
        warn('this endpoint is no longer valid')
        # The post function has to do a few things
        # It needs to execute the basic query handling
        # This includes: Preprocessing, verb extraction
        # Tree traversal, and search result posting
        form = QueryRequestForm(request.POST)
        if form.is_valid():
            # now you can extract the cleaned query
            # I.E the query without any short unnecessary words
            query = form.cleaned_data.get('query')
            #category = get_category_for_verb(query)
            entity_list = get_entity_list(query)
            # we are going to return the top ten profiles for the given entities in this list
            i = 0
            profiles = []
            while (len(profiles) < page_limit):
                profiles = get_profile_for_entity(entity_list[i], page_limit)
                i = i + 1
            data = {
                     'query': query,
                     #'category': category,
                     'entity_list': entity_list,
                     'profiles': profiles,
            }

            # Temporarily just return the simple query cleaned
            return render(request, 'query_parser/query_result.html', data)

class AskSearchView(View):
    """
    This is the Main google like search view
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/LearnLive.html')

    def post(self, request, *args, **kwargs):
        # The post function has to do a few things
        # It needs to execute the basic query handling
        # This includes: Preprocessing, verb extraction
        # Tree traversal, and search result posting
        return redirect("/v2?query=" + request.POST.get('query'));


class ProcessSearchView(View):

    def get(self, request, *args, **kwargs):
        # It needs to execute the basic query handling
        # This includes: Preprocessing, verb extraction
        # Tree traversal, and search result posting
        form = QueryRequestForm(request.GET)
        if form.is_valid():
            # now you can extract the cleaned query
            # I.E the query without any short unnecessary words
            query = form.cleaned_data.get('query')
            #category = get_category_for_verb(query)
            entity_list = get_entity_list(query)
            profile_list = []
            page_limit = 10
            if len(entity_list) > 0:
                i = 0
                while (len(profile_list) < page_limit and i < len(entity_list)):
                    tmp_profile_list = get_profile_for_entity(entity_list[i], 0, page_limit - len(profile_list))
                    for item in tmp_profile_list:
                        if item not in profile_list:
                            profile_list.append(item)
                    i = i + 1
            data = {
                     'query': query,
                     'profiles': profile_list,
                     #'category': category,
                     'entity_list': entity_list,
            }

            # Temporarily just return the simple query cleaned
            return render(request, 'query_parser/bidprofile.html', data)

        return render(request, 'query_parser/LearnLive.html')


class AlternateSearchView(View):
    """
    Search rewrite View
    """

    def get(self, request, *args, **kwargs):
        form = QueryRequestForm(request.GET);
        if form.is_valid():
            query = form.cleaned_data.get('query');

            # pass the query into a natural language processing pipeline
            # output is list of tokens
            tokens = tokenize_query(query)

            # find the NE from the given tokens
            # output is a list of profiles that mathed the named entities
            named_profiles = get_NE(query)

            # match the rest of the tokens to potential skills
            # must be a sorted list by score
            skill_list = get_skills(tokens)
            ret_list = []

            for i in range(0,min(15, len(skill_list))):
                ret_list.append(skill_list[i])

            data = {
                    'query': query,
                    'skills': ret_list,
            }

            return render(request, 'query_parser/bidprofile2.html', data)

        return render(request, 'query_parser/LearnLive.html')


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/instructorprofile.html')

class SearchResults(View):

    def get(self, request, *args, **kwargs):
        warn("TESTING PURPOSE ONLY")
        return render(request, 'query_parser/bidprofile.html')

class AboutUs(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/aboutus.html')

    def post(self, request, *args, **kwargs):
        form = LeaveMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            lm = LeaveMessage(name=name, email=email, phone=phone, message=message)
            lm.save()

        return render(request, 'query_parser/aboutus.html')

class Confirm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/confirmation.html')

