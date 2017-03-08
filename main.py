# Text Stats
# Author: traillj

import frequent_words as fw

NUM_FREQUENT_WORDS = 20
CONTENT_FILENAME = "data/content1.txt"
EXCLUDE_FILENAME = "data/exclude1.txt"


def main():
    """
    Prints statistics related to the text in a file.
    """
    with open(CONTENT_FILENAME) as file:
        content = file.readlines()
    content = [x.strip() for x in content]

    with open(EXCLUDE_FILENAME) as file:
        exclude = file.readlines()
    exclude = [x.strip().lower() for x in exclude]

    freq_list = fw.get_frequent_words(content, exclude, NUM_FREQUENT_WORDS)
    print_freq_list(freq_list)
    print_num_excluded(freq_list, content, exclude)


def print_freq_list(freq_list):
    """
    Prints the frequent words in a formatted manner.
    INPUT:
        freq_list = Most frequent words list, each item
                    a tuple of the form: (word, count).
    """
    rank = 1
    for item in freq_list:
        print("{0:2d}. {1:14s} {2:8d}".format(rank, item[0], item[1]))
        rank += 1


def print_num_excluded(freq_list, content, exclude):
    """
    Prints the number of excluded words that appeared more
    times than the last ranked word of the most frequent list.
    INPUT:
        freq_list = Most frequent words list, each item
                    a tuple of the form: (word, count).
        content = List of lines containing words.
        exclude = List of words that were excluded.
    """
    last_rank_item = freq_list[-1]
    last_rank_count = last_rank_item[1]
    num_excluded = fw.count_more_frequent(content, exclude,
                                          last_rank_count)
    out = "\n{0} excluded words appeared more than {1} times."
    print(out.format(num_excluded, last_rank_count))


main()
