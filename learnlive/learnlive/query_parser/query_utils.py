# This file is the property of Qurious Inc.
# By Abhinav Khanna
# Purpose: this is a utility file for handling the parsing of queries.
from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from text.wordnet import Synset

from learnlive.query_parser.models import Verb

def get_category_for_verb(query):
    """
    The job of this function is to parse out the verb
    and understand a basic category that the verb can be placed into
    by looking at the current hash table of values available.
    It looks at a wordnet approximation to the words in the Hashtable
    mapping to the closest category assignemnt if none is readily available
    """
    avg_list = []
    pos_list = TextBlob(query).tags
    verb = [v for i, v in enumerate(pos_list) if v[1] == 'VRB' or v[1] == 'VRZ' or v[1] == 'VB' or v[1] == 'VBP'] # searches for that VERB bitches

    # for now if the lexical interpreter can't figure out what the verb is this part just jumps ship
    if len(verb) == 0:
        # scan all words and see if they are in our verb database, if they aren't we just throw up our hands
        blob = TextBlob(query).words
        for word in blob:
            db_entry = Verb.objects.filter(name=word)
            if len(db_entry) != 0:
                return db_entry[0].categories.values()
        return;

    verb, pos = verb[0]
    kb_list = Verb.objects.filter(name=verb)
    query_syn = Word(verb).get_synsets(pos=VERB)
    if len(kb_list) == 0:
        # this means you don't have a direct match, need to parse through the entire tree
        kb_list = Verb.objects.filter()
        # you need to get the synset of the query_verb and the synset of the kb_verb
        for kb_verb in kb_list:
            kb_syn = Word(kb_verb.name).get_synsets(pos=VERB)
            sim_sum = 0
            count = 0
            for syn in query_syn:
                for syn2 in kb_syn:
                    sim_sum += syn.wup_similarity(syn2)
                    sim_sum += syn.lch_similarity(syn2)
                    sim_sum += syn.path_similarity(syn2)
                    count += 1
            # enqueue the avg into its spot in the array
            avg = sim_sum / count
            avg_list.append(avg)

        # Scan the avg_list for the max entry
        print avg_list
        print kb_list
        index = avg_list.index(max(avg_list))
        new_verb = Verb(name=verb)
        new_verb.save()

        for category in kb_list[index].categories.all():
            new_verb.categories.add(category)

        return kb_list[index].categories.values()
    else:
        return kb_list[0].categories.values()
