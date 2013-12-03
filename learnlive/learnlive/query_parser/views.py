# Create your views here.
# This code is the property of Learnlive Inc
# Written by Abhinav Khanna

from django.views.generic import View
from django.shortcuts import render
from warnings import warn
from learnlive.query_parser.query_utils import get_category_for_verb
from learnlive.query_parser.query_utils import get_entity_list
from learnlive.bid_platform.skill_utils import get_profile_for_entity

from learnlive.query_parser.forms import QueryRequestForm


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
        form = QueryRequestForm(request.POST)
        if form.is_valid():
            # now you can extract the cleaned query
            # I.E the query without any short unnecessary words
            query = form.cleaned_data.get('query')
            #category = get_category_for_verb(query)
            entity_list = get_entity_list(query)
            profile_list = []
            if len(entity_list) > 0:
                profile_list = get_profile_for_entity(entity_list[0], 0, 10)

            data = {
                     'query': query,
                     'profiles': profile_list,
                     #'category': category,
                     'entity_list': entity_list,
            }

            # Temporarily just return the simple query cleaned
            return render(request, 'query_parser/bidprofile.html', data)

        return render(request, 'query_parser/LearnLive.html')

class ProfileView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/instructorprofile.html')

class SearchResults(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/bidprofile.html')

class InClassView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/inclass.html')
