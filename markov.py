"""Generate Markov text from text files."""

from random import choice

import sys

input_path = sys.argv[1]

def open_and_read_file(file_path=input_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # open file
    with open(file_path) as file:

        # add everything in file to text as one string
        text = file.read()

    # return string of all the text
    return text

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    # create list of words, splitting text string at each whitespace
    words = text_string.split()
    # print(words)

    # create empty dictionary
    chains = {}

    # iterate over index values
    for i in range(len(words) - 2):

        # define first, second, and third words
        first_word = words[i]
        second_word = words[i+1]
        third_word = words[i+2]

        # create tuple from first and second word
        pair = (first_word, second_word)

        # create tuple: next word dict entry. initialize list if tuple is new, add third word to list.
        chains[pair] = chains.get(pair, []) + [third_word]
    
    # return the chains dictionary
    return chains


def make_text(chains):
    """Return text from chains."""

    # initialize blank words list
    words = []

    # Get first and second word / get first tuple
    for key in chains:
        first_word = key[0]
        second_word = key[1]
        words.extend([first_word, second_word])
        break
    
    # get tuple key from last two words in list
    
    # psuedocode
    # use the second word and a random word from the key's value to make a new tuple (second_word, random_value_word)
    # repeat this over and over until we get to the end

    while True:
        # find random next word by using previous two words as tuple and next word from values
        random_value_word = choice(chains[(first_word, second_word)])
        
        # reassign first and second word values
        first_word = second_word
        second_word = random_value_word

        # add new second word to 'words' list
        words.extend([second_word])
        print(words)
        break

    return #' '.join(words)



# Open the file and turn it into one long string
input_text = open_and_read_file()

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
