# This file is the property of Qurious Inc.
# By Abhinav Khanna
# Purpose: this is a utility file for handling the parsing of queries.
import nltk;
from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from textblob.wordnet import Synset
from nltk.stem.wordnet import WordNetLemmatizer

from learnlive.query_parser.models import Verb
from learnlive.bid_platform.models import Skill
from learnlive.query_parser.models import Entity

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

def load_scraped_info(filename):
    f = open(filename)
    line = f.readline()

    while len(line) != 0:
        line = line.replace(';','')
        line = line.replace('\n', '')
        line = line.replace('\\n', '')
        category = line.split(':')
        children = category[1]
        category = category[0].lower()
        childarray = children.split(' ')
        entity = Entity.objects.filter(name=category)
        if len(entity) == 0:
            # no entity currently exists add a new one.
            url = 'http://en.wikipedia.org/wiki/' + category
            entity = [Entity.add_root(name=category, wiki_page=url)]

        for e in entity:
            # now add the children
            for child in childarray:
                if child != '':
                    # i.e the child hadn't been added yet
                    root = Entity.objects.get(pk=e.id)
                    url = 'http://en.wikipedia.org/wiki/' + child
                    child = child.lower()
                    children_set = root.get_children().filter(name=child)
                    if len(children_set) == 0:
                        root.add_child(name=child, wiki_page=url)

        line = f.readline()

def get_entity_list(query):
    """
    This function's only job is to get the list of relevant entries given a query
    """
    search_query = query;
    final_list = []
    pos_list = TextBlob(query).tags
#    query = TextBlob(query).noun_phrases
    # we now have a valid query object that does not have a verb in it :D begin
    # the longest prefix matching process!!!
    # for now just do the direct matching program....
    # and if that returns null, just do the noun and see if that comes up
#    if len(query) != 0:
#        for item in query:
#            # normalize the item
#            item = item.replace(' ', '_')
#            entity_list = Entity.objects.filter(name=item)
#            if len(entity_list) == 0:
#                final_list = get_entities_by_permute(item, pos_list, final_list)
#            else:
#                for e in entity_list:
#                    final_list.append(e)
#    else:
    final_list = get_entities_by_permute(search_query, pos_list, final_list)

    return final_list

def get_entities_by_permute(search_query, pos_list, final_list):
    """
    Gets the entities that match to any given permutation of the words
    """
    # we need to remove the verb from the query
    words = []
    for (word, pos) in pos_list:
        if 'JJ' in pos or 'FW' in pos or 'JJ' in pos or 'NN' in pos or 'PS' in pos or 'RB' in pos or 'VBG' in pos:
            words.append(word)

    # now that we have removed the verb :D.
    # we want to basically take the longest matching prefix check if thats in the db, and try again
    for j in range(0, len(words)):
        string = ''
        for i in range(j, len(words)):
            if i != len(words) - 1:
                string += words[i] + "_"
            else:
                string += words[i]
        # check the db for this string
        e = Entity.objects.filter(name=string)
        if len(e) == 0:
            # try switching the plurality of the word
            if string[-1] == 's':
                string = string.replace(string[-1], '')
            else:
                string += 's'

        e = Entity.objects.filter(name=string)
        if len(e) > 0:
            for entity in e:
                final_list.append(entity)
            return final_list

    # signifies no matches were found
    return [];

def get_entities_with_nouns(search_query, pos_list, final_list):
        # the full prefix didn't match, try permutations.
        # but for now just return the entities that match the nouns.
        noun_list = [n for i, n in enumerate(pos_list) if n[1] == 'NN' or n[1] == 'NNP' or n[1] == 'NNS'] # searches for that VERB bitches
        if len(noun_list) == 0:
            # no nouns return not recognized;
            # now just try every single word in the pos_list and return those as relevant, relevance increases based on size;
            for (word, pos) in pos_list:
                # normalize the word
                word = word.replace(' ', '_')
                entities = Entity.objects.filter(name=word)
                if len(entities) >= 0:
                    for e in entities:
                        final_list.append(e)
        else:
            for noun in noun_list:
                # check if the noun is in our db
                # normalize the noun
                noun = noun[0].replace(' ', '_')
                db_noun = Entity.objects.filter(name=noun)
                for db_n in db_noun:
                    final_list.append(db_n)
                    db_n.add_child(name=search_query)

        return final_list

def tokenize_query(query):
    """
    This function will produce the tokenizations of the query:
    POS tags the query
    Tokenizes single word the query
    Multi word (2) tokenizes the query
    """
    tokens = nltk.word_tokenize(query)
    pos_tokens = nltk.pos_tag(tokens)
    multi_word_tokens = []

    # make the multi word tokens now
    past_word = '' 
    for (word, pos) in pos_tokens:
        if past_word == '':
            past_word = word
        else:
            combined_word = (past_word + ' ' + word, '')
            multi_word_tokens.append(combined_word)
            past_word = word

    merged_token_list = pos_tokens + multi_word_tokens
    return merged_token_list

def get_NE(query):
    """
    This function returns a list of named entity tuples of the form (named_entity, POS)
    """
    import pdb; pdb.set_trace()
    tokens = nltk.word_tokenize(query)
    NE_tokens = nltk.ne_chunk(tokens, binary=True)
    ne_list = []

    for token in NE_tokens:
        if hasattr(token, 'node') and token.node:
            if token.node == 'NE':
                profiles = UserProfile.objects.filter(profile_name=token[0][0])
                ne_list = ne_list + profiles

    return ne_list

def get_entities_for_skill(skill_name):
    """
    Returns an entity for the given skill object or null
    """
    name = skill_name.replace(' ', '_')
    entity_list = Entity.objects.filter(name=name)
    return entity_list

def get_skill_for_entity(entity_name):

    lmtzr = WordNetLemmatizer()
    name = entity_name.replace('_', ' ')
    lemma = lmtzr.lemmatize(name)
    skills = Skill.objects.filter(lemma_name=lemma)
    return skills


def get_skills(tokens):
    """
    Takes in a complete list of tokens and finds the skills that match, and scores them
    the tuple that it presents is (score, skill)
    """
    lmtzr = WordNetLemmatizer()
    skill_list = []
    for token in tokens:
        lemma = lmtzr.lemmatize(token[0])
        skills = Skill.objects.filter(lemma_name=lemma)
        score = 0
        if 'NN' in token[1]:
            score = 5
        elif 'VB' in token[1]:
            score = 2
        elif 'JJ' in token[1]:
            score = 4
        elif token[1] == '':
            # compound word
            score = 6
        else:
            score = 1
        for skill in skills:
            skill_list.append((score, skill))

        # time to check the children and parents
        if len(skills) == 0:
            continue

        entity_list = get_entities_for_skill(skills[0].name)
        for entity in entity_list:
            children = entity.get_children()
            for child in children:
                child_skills = get_skill_for_entity(child.name)
                for skill in child_skills:
                    if (score, skill) not in skill_list:
                        skill_list.append((score * 0.75, skill))

            parent = entity.get_parent()
            parent_skills = get_skill_for_entity(parent.name)
            for skill in parent_skills:
                if (score, skill) not in skill_list:
                    skill_list.append((score * 0.5, skill))

    skill_list = sorted(skill_list, reverse=True)
    return skill_list




