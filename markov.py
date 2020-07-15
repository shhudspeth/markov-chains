"""Generate Markov text from text files."""

from random import choice
import sys



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


def make_chains(text_string, n_gram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
     to make a n-gram... would need to use an *arg list... for x in *arg, len(arg)
     # found the tuple(list) idea from here : https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/#:~:text=Itertools.Permutations()-,Python%20%7C%20Convert%20a%20list%20into%20a%20tuple,given%20list%20into%20a%20tuple.&text=Approach%20%231%20%3A%20Using%20tuple(,simply%20using%20tuple(list_name).
     for x in range(len(arg))
     key = text[:n]
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
    
    n_gram = int(n_gram)
    # loop over text with indices, stop n-gram away
    for word in range(len(text)-n_gram):
        # set key tuple of n-gram words
        key_tuple = tuple(text[word:word+n_gram])
        # get current next word list
        next_word_list = chains.get(key_tuple,[])
        # append the next word to list
        next_word_list.append(text[word+n_gram]) 
        # set new next word list as the dictionary entry 
        chains[key_tuple] = next_word_list
        
    # set last n-gram as stop phrase           
    key_tuple = tuple(text[word:word+n_gram])
    chains[key_tuple] = None
            
    # # print dictionary
    # for tuple_, list_ in chains.items():
    #     print(f"n-gram: {tuple_}, \n options: {list_}")

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    not_end_of_list = True
    # your code goes here
    # use random.choice to pick a bigram element from keys
    # make a list of capitalized keys? make a list of punctuation?
    while not_end_of_list:
        choice_n = choice(list(chains.keys()))
        # add bigram key  to word list
        words.extend(choice_n)
        if chains[choice_n]:
            choose_third = choice(chains[choice_n])
            words.append(choose_third)
            # print(words)
        else:
            not_end_of_list = False

    return " ".join(words)



if __name__ == '__main__':
    # python3 markov text.txt no_n_grams
    input_path = sys.argv[1]
    n_grams = sys.argv[2]
    print(n_grams)
    # Open the file and turn it into one long string
    input_text = open_and_read_file(input_path)
    # Get a Markov chain
    chains = make_chains(input_text,n_grams)
    # Produce random text
    random_text = make_text(chains)
    print(random_text)
