"""
Write a Python program named sentences.py that generates simple English sentences. 
During this prove milestone, you will write functions that generate sentences with three parts:

a determiner (sometimes known as an article)
a noun
a verb
For example:

A cat laughed.
One man eats.
The woman will think.
Some girls thought.
Many dogs run.
Many men will write.
For this milestone, your program must include at least these five functions:

main
make_sentence
get_determiner
get_noun
get_verb
You may add other functions if you want. The functions get_determiner, get_noun, 
and get_verb, must randomly choose a word from a list of words and return the 
randomly chosen word. All the functions that you must write for this milestone 
assignment are described in the Steps section below.

Use the get_determiner function from the previous lesson’s prove milestone as an example to help you write the get_preposition function. The get_preposition function must have the following header and fulfill the requirements of the following documentation string.
def get_preposition():
    Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    
Write the get_prepositional_phrase function to have the following header and fulfill the requirements of the following documentation string.
def get_prepositional_phrase(quantity):
    Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    
Add code to the make_sentence function and write any other functions that you think are necessary for your program to generate and print six sentences, each with a determiner, a noun, a verb, and a prepositional phrase. The six sentences must have the following characteristics:

Quantity	Verb Tense
a.	single	past
b.	single	present
c.	single	future
d.	plural	past
e.	plural	present
f.	plural	future


"""

import random
"""
Write the main function to call your make_sentence function six times and print six sentences with these characteristics:

Quantity	Verb Tense
a.	single	past
b.	single	present
c.	single	future
d.	plural	past
e.	plural	present
f.	plural	future

"""

def main():

    word = get_determiner(1).capitalize()
    noun = get_noun(1)
    verb = get_verb(1, "past")
    prepositional_phrase = get_prepositional_phrase(1)
    sentence = make_sentence(1, "past", word, noun, verb, prepositional_phrase)
    print(sentence)
    word = get_determiner(1).capitalize()
    noun = get_noun(1)
    verb = get_verb(1, "present")
    prepositional_phrase = get_prepositional_phrase(1)
    sentence = make_sentence(1, "present", word, noun, verb, prepositional_phrase)
    print(sentence)
    word = get_determiner(1).capitalize()
    noun = get_noun(1)
    verb = get_verb(1, "future")
    prepositional_phrase = get_prepositional_phrase(1)
    sentence = make_sentence(1, "future", word, noun, verb, prepositional_phrase)
    print(sentence)
    word = get_determiner(2).capitalize()
    noun = get_noun(2)
    verb = get_verb(2, "past")
    prepositional_phrase = get_prepositional_phrase(2)
    sentence = make_sentence(2, "past", word, noun, verb, prepositional_phrase)
    print(sentence)
    word = get_determiner(2).capitalize()
    noun = get_noun(2)
    verb = get_verb(2, "present")
    prepositional_phrase = get_prepositional_phrase(2)
    sentence = make_sentence(2, "present", word, noun, verb, prepositional_phrase)
    print(sentence)
    word = get_determiner(2).capitalize()
    noun = get_noun(2)
    verb = get_verb(2, "future")
    prepositional_phrase = get_prepositional_phrase(2)
    sentence = make_sentence(2, "future", word, noun, verb, prepositional_phrase)
    print(sentence)

    pass

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.lower() == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense.lower() == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense.lower() == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
        
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    word = get_determiner(quantity) 
    noun = get_noun(quantity)

    prepositional_phrase = f'{preposition} {word} {noun}'

    return prepositional_phrase

def make_sentence(quantity, tense, word, noun, verb, prepositional_phrase):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    if tense.lower() == "past":
        sentence = f'{word} {noun} {verb} {prepositional_phrase}.'
    elif tense.lower() == "present":
        if quantity == 1:
            sentence = f'{word} {noun} {verb} {prepositional_phrase}.'
        else:
            sentence = f'{word} {noun} {verb} {prepositional_phrase}.'

    elif tense.lower() == "future":
        sentence = f'{word} {noun} {verb} {prepositional_phrase}.'

    return sentence

main()
