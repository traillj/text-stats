# Text Stats
# Author: traillj


def count_matches(phrase, content):
    """
    Counts the number of times phrase appears in content.
    INPUT:
        phrase = A list with the words as separate items.
        content = List of lines containing words.
    """
    count = 0

    for line in content:
        words = line.split()
        words = [word.strip(",'`.;\"!():?").lower() for word in words]

        for i in range(len(words) - len(phrase) + 1):
            words_index = i

            for j in range(len(phrase)):
                if words[words_index] != phrase[j]:
                    break
                if j == len(phrase) - 1:
                    count += 1
                else:
                    words_index += 1
    return count
