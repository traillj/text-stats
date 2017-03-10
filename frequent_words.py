# Text Stats
# Author: traillj
#
# Ranks the most frequent words in a file.
# Can include a list of words to exclude.

import operator
import word_stats


def get_frequent_words(content, exclude, size):
    """
    Gets the most frequent words with the count in order.
    INPUT:
        content = List of lines containing words.
        exclude = List of words to be excluded.
        size = Number of words to return.
    RETURN:
        A list with rank_size items, each item a tuple
        of the form: (word, count).
    """
    freq = create_freq_dict(content, exclude)
    freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
    rank = 1
    most_freq = []

    for item in freq:
        most_freq.append(item)
        rank += 1
        if rank > size:
            break
    return most_freq


def create_freq_dict(content, exclude):
    """
    Creates a dict of word frequencies. The key are
    the words that appear in the text file and the
    value is the number of times each word appears.
    INPUT:
        content = List of lines containing words.
        exclude = List of words to be excluded.
    RETURN:
        A dict of word keys and count values.
    """
    freq = {}
    # Add the words to be excluded
    for word in exclude:
        freq[word] = -2**31

    for line in content:
        words = word_stats.get_words(line)
        for word in words:
            freq.setdefault(word, 0)
            freq[word] = freq[word] + 1

    freq = remove_negative_count(freq)
    return freq


def remove_negative_count(freq):
    """
    Creates a new dict that does not include
    words that have a count smaller than one.
    INPUT:
        freq = Dict of word keys and count values.
    RETURN:
        A new dict with only positive counts.
    """
    new_freq = {}
    for (word, count) in freq.items():
        if count > 0:
            new_freq[word] = count
    return new_freq


def count_more_frequent(content, words, min_count):
    """
    Gets the number of words that appear more
    times than the minimum count.
    INPUT:
        content = List of lines containing words.
        words = List of words to test.
        min_count = Minimum count considered.
    RETURN:
        The number of words that are frequent.
    """
    freq = {}
    for word in words:
        freq[word] = 0

    for line in content:
        words = word_stats.get_words(line)
        for word in words:
            if freq.get(word) is not None:
                freq[word] = freq[word] + 1

    freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
    count = 0
    for item in freq:
        if item[1] > min_count:
            count += 1
        else:
            break
    return count
