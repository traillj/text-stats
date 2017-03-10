# Text Stats
# Author: traillj

import frequent_words as fw
import word_stats


# Number of frequent words to print.
# Set to zero to not print frequent words.
NUM_FREQUENT_WORDS = 20

# The text to be analysed.
CONTENT_FILENAME = "data/content1.txt"

# Words to be excluded, one word per line.
EXCLUDE_FILENAME = "data/exclude1.txt"

# Only include alphanumeric characters and spaces,
# one phrase per line.
PHRASES_FILENAME = "data/phrases1.txt"


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

    if NUM_FREQUENT_WORDS > 0:
        freq_list = fw.get_frequent_words(content, exclude, NUM_FREQUENT_WORDS)
        print_freq_list(freq_list)
        print()
        print_num_excluded(freq_list, content, exclude)
        print("\n")

    print_phrase_counts(PHRASES_FILENAME, content)
    print("\n")
    print_word_stats(content)


def print_freq_list(freq_list):
    """
    Prints the frequent words in a formatted manner.
    INPUT:
        freq_list = Most frequent words list, each item
                    a tuple of the form: (word, count).
    """
    print(" ----- Frequent Words -----")
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
    out = "{0} excluded words appeared more than {1} times."
    print(out.format(num_excluded, last_rank_count))


def print_phrase_counts(phrases_filename, content):
    """
    Prints phrase counts in a formatted manner.
    INPUT:
        phrases_filename = File of phrases, one per line, with
                           only alphanumeric characters and spaces
        content = List of lines containing words.
    """
    with open(phrases_filename) as file:
        phrases = file.readlines()
    phrases = [x.strip().lower() for x in phrases]

    if len(phrases) > 0:
        print("------------ Phrase Counts ------------")
        for phrase in phrases:
            phrase_words = phrase.split()
            count = word_stats.count_matches(phrase_words, content)
            print("{0:30s} {1:8d}".format(phrase, count))


def print_word_stats(content):
    """
    Prints the word count, average word length and longest words.
    INPUT:
        content = List of lines containing words.
    """
    print("---------------- Word Stats ----------------")

    word_count = word_stats.count_words(content)
    print("Word Count: {0}".format(word_count))

    avg_word_len = word_stats.get_avg_word_len(content)
    print("Average Word Length: {0:.2f}".format(avg_word_len))

    longest_words = word_stats.get_longest_words(content)
    print("Longest Words: {0}".format(", ".join(longest_words)))


main()
