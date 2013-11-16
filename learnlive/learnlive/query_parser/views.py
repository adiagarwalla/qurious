# Create your views here.
# This code is the property of Learnlive Inc
# Written by Abhinav Khanna

from django.views.generic import View
from django.shortcuts import render
from learnlive.query_parser.query_utils import get_category_for_verb

from learnlive.query_parser.forms import QueryRequestForm

class AskQueryView(View):
    """
    This is the view for the main landing page
    where a query can be inserted. I.E the home landing
    page that looks like google's.
    """

    def get(self, request, *args, **kwargs):
        form = QueryRequestForm()
        return render(request, 'query_parser/query.html', {'form': form})

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
            category = get_category_for_verb(query)
            entity_list = get_entity_list(query)
            data = {
                     'query': query,
                     'category': category
            }

            # Temporarily just return the simple query cleaned
            return render(request, 'query_parser/query_result.html', data)

class AskSearchView(View):
    """
    This is the testing view to test search page
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'query_parser/Learnlive.html')
