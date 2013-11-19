# Create your forms here
# This class is property of LearnLive Inc.
# This class was written by Abhinav Khanna
from django import forms
from textblob import TextBlob

class QueryRequestForm(forms.Form):
    query = forms.CharField()

    def clean_query(self):
        # remove all unnecessary words and phrases
        # all words under or at 2 chars of length will be removed
        query = self.cleaned_data.get('query')
        query = query.lower()
        textblob = TextBlob(query)
        wordlist_words = textblob.words
        words = []
        for word in wordlist_words:
            words.append(word)
        length = len(words)
        x = 0
        while x < length:
            if len(words[x]) < 3 and words[x] != 'to':
                words[x] = ""
            x = x + 1

        # combine all the strings to recreate the now stripped string
        stripped_string = ""
        for x in range(0, length):
            # we only want to include the non WRB words
            if words[x] != '':
                text_analyzer = TextBlob(words[x])
                analysis = text_analyzer.tags
                pairs = analysis[0]
                value = pairs[1]
                if value != 'WRB' and value != 'WDT' and value != 'WP' and value != 'WP$':
                    stripped_string += words[x]
                    stripped_string += " "

        # strip leading white spaces
        query = stripped_string.lstrip()

        return query

