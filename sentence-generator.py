import random

noun_list = ["dog", "cat", "computer", "donut", "ice cream", "snapchat"]
verb_list = ["eats", "hugs", "screams", "roars", "sleeps"]
adjective_list = ["happy", "tasty", "lovely", "devlish", "red", "heavy"]
adverb_list = ["quickly", "excitedly", "lazily", "loudly", "slowly"]
preposition_list = ["under", "over", "above", "around",]
article_list = ["a", "the"]

#make myself a function for generating noun phrases
def noun_phrase():
    return random.choice(article_list) + " " + \
    random.choice(adjective_list) + " " + \
    random.choice(noun_list) + " "
#make myself a function for generating verb phrases
def verb_phrases():
    return random.choice(adverb_list) + " " + \
    random.choice(verb_list) + " "
#make myself a function for generating preposition phrases
def prepositional_phrases():
    return random.choice(preposition_list) + " " + \
    noun_phrase()
#try out noun phrase generator a few times
print(noun_phrase() + verb_phrases() + prepositional_phrases())


#def sentence():
#    return noun_phrase
