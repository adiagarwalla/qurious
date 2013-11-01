# Create your forms here
# This class is property of LearnLive Inc.
# This class was written by Abhinav Khanna
from django import forms

class QueryRequestForm(forms.Form):
    query = forms.CharField()

    def clean_query(self):
        # remove all unnecessary words and phrases
        # all words under or at 2 chars of length will be removed
        query = self.cleaned_data.get('query')
        words = query.split(" ")
        length = len(words)
        x = 0
        while x < length:
            if len(words[x]) < 3:
                words[x] = ""
            x++

        # combine all the strings to recreate the now stripped string
        stripped_string = ""
        for x in range(0, length):
            stripped_string += words[x]
            stripped_string += " "

        # strip leading white spaces
        query = query.lstrip()

        return query

