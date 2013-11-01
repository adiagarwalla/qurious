# Create your views here.
# This code is the property of Learnlive Inc
# Written by Abhinav Khanna

from django.views.generic import View
from django.shortcuts import render

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
            data = { 'query': query }

            # Temporarily just return the simple query cleaned
            return render(request, 'query_parser/query_result.html', data)
