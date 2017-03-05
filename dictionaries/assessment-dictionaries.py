"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
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

    words = phrase.split()  # Create list of words in phrase split on spaces
    word_counts = {}

    # Populate word_counts dictionary with new words with value 1 or 
    # add 1 to value if word already exists in word_counts
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melons = {'Watermelon': 2.95,
              'Cantaloupe': 2.50,
              'Musk': 3.25,
              'Christmas': 14.25,
              }

    return melons.get(melon_name, 'No price found')

    # ALTERNATIVE SOLUTION:

    # melons = {'Watermelon': 2.95,
    #           'Cantaloupe': 2.50,
    #           'Musk': 3.25,
    #           'Christmas': 14.25,
    #           }

    # price = melons.get(melon_name, 'No price found')
    # return price


    # OTHER ALTERNATIVE:

    # melons = {'Watermelon': 2.95,
    #           'Cantaloupe': 2.50,
    #           'Musk': 3.25,
    #           'Christmas': 14.25,
    #           }

    # if melon_name in melons:
    #     return melons[melon_name]
    # else:
    #     return 'No price found'

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

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    word_lengths = {}

    # Populate word_lengths dictionary with word_length as keys and 
    # words of that length as a value list
    for word in words:
        word_length = len(word)
        word_lengths[word_length] = word_lengths.get(word_length, []) + [word]
    
    sorted_words_by_length = []

    # Add new tuple to sorted_words_by_length with word length and sorted list of words
    for word_length, words in word_lengths.items():
        sorted_words_by_length.append((word_length, sorted(words)))

    # Return sorted_words_by_length list sorted by word length
    return sorted(sorted_words_by_length)


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

    english_pirate_translator = {'sir': 'matey',
                                 'hotel': 'fleabag inn',
                                 'student': 'swabbie',
                                 'man': 'matey',
                                 'professor': 'foul blaggart',
                                 'restaurant': 'galley',
                                 'your': 'yer',
                                 'excuse': 'arr',
                                 'students': 'swabbies',
                                 'are': 'be',
                                 'restroom': 'head',
                                 'my': 'me',
                                 'is': 'be',
                                 }

    words = phrase.split()  # Create a list of words in the original phrase
    new_phrase_words = []  # Create an empty list to hold the translated words

    # Add translated (or original) words to the new_phrase_words list
    for word in words:
        new_phrase_words.append(english_pirate_translator.get(word, word))

    # Join the list of words into the translated string
    new_phrase = " ".join(new_phrase_words)

    return new_phrase


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

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Keys = last letters, Values = list of names that start with that letter
    last_letters = {}

    # Populate last_letters with last letter keys and empty lists as values
    for name in names:
        last_letter = name[-1]
        last_letters[last_letter] = []

    # Add names that start with the last_letters to the value lists,
    # not including first word in names
    for name in names[1:]:
        first_letter = name[0]
        if first_letter in last_letters:
            last_letters[first_letter] += [name]

    # Set up results and loop using first word in names list
    first_word = names[0]
    last_letter = first_word[-1]
    results = [first_word]

    # Run loop until you hit a value list without any names in it
    while len(last_letters[last_letter]):
        # Capture and remove first item in value list as name
        name = last_letters[last_letter].pop(0)
        results.append(name)
        last_letter = name[-1]

    return results




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


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
