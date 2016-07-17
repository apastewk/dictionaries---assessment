"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    word_count = {}
    phrase = phrase.split(" ")
    
    for word in phrase:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """
    melon_data = {"Watermelon": 2.95, 
                  "Cantaloupe": 2.50, 
                  "Musk": 3.25, 
                  "Christmas": 14.25
                  }

    
    if melon_data.get(melon_name):
        return melon_data[melon_name]
    else:
        return "No price found" 


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    word_length_count = {}

    for word in words:
        if len(word) in word_length_count:
            word_length_count[len(word)] += [word]
        else:
            word_length_count[len(word)] = [word]


    ordered_count = []
    for key, value in word_length_count.items():
        ordered_tuple = key, sorted(value)
        ordered_count.append(ordered_tuple)

    return ordered_count


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

 
    pirate_talk_phrase = ""
    english_phrase = phrase.split(" ")

    translated_words = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie",
                        "man": "matey", "professor": "foul blaggart", 
                        "restaurant": "galley", "your": "yer", "excuse": "arr", 
                        "students": "swabbies", "are": "be", "restroom": "head", 
                        "my": "me", "is": "be"
                        }
    
    for word in english_phrase:
        if translated_words.get(word, 0) == 0:
            pirate_talk_word = word
            pirate_talk_phrase += pirate_talk_word + " " 
        else:
            pirate_talk_word = translated_words[word]
            pirate_talk_phrase += pirate_talk_word + " "

    return pirate_talk_phrase.rstrip()

    # I tried the format method but I didn't know how to get rid of the space at
    # the beginning of the string.  


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

     
# I am not sure how to use a dictionary, it seems to make things more confusing
# Don't know what to put as key and what to put as value 
# This was me trying to use a dictionary

#     word_chain = {}
#     lst = []
#     count = 1
#     next_key = names[count]
    
#     for name in names:
#         word_chain[name] = name[-1]
#         last_letter = word_chain[name]
#         print word_chain

 
#     for next_key in word_chain:
#         print "last:", last_letter
#         print "next_key:", next_key
#         if last_letter == next_key[0]:
#             print "yayyy!"
#             lst.append(next_key)
#             next_key 
#             count += 1


            # print "name:", name
            # print "next_key:", next_key
            # print "last:", last_letter
            # print "next:", next_key[0]
            # if last_letter == next_key[0]:
            #     print last_letter
            #     print next_key[0]
            #     lst.append(next_key)
            #     print lst
            #     continue

    
# This is me trying without a dictionary.  I got this one closer but couldn't think
# of how to get myself out of the infinite loop 


    # count = 1
    # first = names[count]
    # master = []
    # name = names[0]
    # master.append(names[0])
    # while True:
    #     for first in names:
    #         print "name:", name
    #         print "first:", first
    #         if name[-1] == first[0] and first not in master:
    #             master.append(first)
    #             count += 1
    #             name = first
    #             print name 
    #             break
    #         else:
    #             count += 1
    #             continue
    #     if name[-1] != first[0]:
    #         return
    #     if len(master) == 0:
    #         return 
    #     # count += 1
    #     # # first = names[count]
    # print master

       
# Other random stuff 


        # while last_letter == :
        #     # print names 
        #     # print name[0]
        #     # print last_letter, word_chain[name]
        #     if last_letter == 
        #         return name 
        #         # print name, name[0], last_letter
        #         # lst.append(name)
        #     # else:
        #     #     return 
        #         # print word_chain

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
