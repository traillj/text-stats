# Text Stats
# Author: traillj
#
# Functions that provide statistics on
# the words in a text. Hyphenated words are split.


def count_matches(phrase, content):
    """
    Counts the number of times phrase appears in content.
    INPUT:
        phrase = A list with the words as separate items.
        content = List of lines containing words.
    """
    count = 0

    for line in content:
        words = get_words(line)
        for i in range(len(words) - len(phrase) + 1):
            words_index = i

            for j, phrase_word in enumerate(phrase):
                if words[words_index] != phrase_word:
                    break
                if j == len(phrase) - 1:
                    count += 1
                else:
                    words_index += 1
    return count


def get_words(line):
    """
    Gets the words from a line, removing common punctuation
    marks at the beginning and end of each word.
    Hyphenated words are split.
    INPUT:
        line = String of words.
    RETURN:
        A list of words.
    """
    line = replace_hyphens(' ', line)
    words = line.split()
    return [word.strip(",'`.;\"!():?").lower() for word in words]


def replace_hyphens(replace_string, line):
    """
    Replaces hyphens with the specified string.
    INPUT:
        replace_string = String to replace hyphen with.
        line = String of words.
    RETURN:
        A new string representing the
        line with the hyphens replaced.
    """
    out = []
    for char in line:
        if char == '-':
            out.append(replace_string)
        else:
            out.append(char)

    return ''.join(out)


def count_words(content):
    """
    Calculates the word count.
    INPUT:
        content = List of lines containing words.
    RETURN:
        The word count.
    """
    count = 0
    for line in content:
        words = get_words(line)
        count += len(words)
    return count


def get_avg_word_len(content):
    """
    Calculates the average word length.
    INPUT:
        content = List of lines containing words.
    RETURN:
        The average word length.
    """
    count_chars = 0
    for line in content:
        words = get_words(line)

        for word in words:
            count_chars += len(word)
    return count_chars / count_words(content)


def get_longest_words(content):
    """
    Creates a set of the longest words.
    INPUT:
        content = List of lines containing words.
    RETURN:
        The longest words.
    """
    longest_len = 0
    longest_words = []
    for line in content:
        words = get_words(line)

        for word in words:
            word_len = len(word)
            if word_len > longest_len:
                longest_words = [word]
                longest_len = word_len
            elif word_len >= longest_len:
                longest_words.append(word)
    return set(longest_words)
