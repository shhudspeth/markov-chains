"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    Example:
    >>> open_and_read_file("green-eggs.txt")
    'Would you could you in a house?\nWould you could you with a mouse?\n
    Would you could you in a box?\nWould you could you with a fox?\n
    Would you like green eggs and ham?\nWould you like them, Sam I am?\n'
    """

    # your code goes here
    file_ = open(file_path).read()

    return file_


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text = text_string.split()
    # print(text)
    len_text = len(text)
    # your code goes here
    for word, idx in enumerate(text):
        
        if word + 2 < len_text:
            # print(text[word], text[word+1], text[word+2])
            if (text[word], text[word+1]) in chains.keys():
                # print("tuple already in dictionary")
                value_list = chains[(text[word], text[word+1])]
                # print(chains[(text[word], text[word+1])], value_list)
                # print("already in list")
                # print(value_list)
                if len(value_list) > 0: 
                    value_list.append(text[word+2])
                    chains[(text[word], text[word+1])] = value_list
                    # print(len(chains[(text[word], text[word+1])]))
                else:
                    value_list = [text[word+2]]
                    # print(value_list, "trying to get rid of none")
                    chains[(text[word], text[word+1])] = value_list
                # need to extend list this the value
            else:
                # print("not in dictionary, making tuples")
                chains[(text[word], text[word+1])] = chains.get((text[word], text[word+1]),[text[word+2]])
                #print("first addition",chains[(text[word], text[word+1])] )
            

    for tuple_, list_ in chains.items():
        print(f"n-gram: {tuple_}, \n options: {list_}")

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
