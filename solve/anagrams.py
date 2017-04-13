import functools as ft
import pdb


def normalize(word):
    return ''.join(sorted(word.replace(' ', '')))


def is_eq(w1, w2):
    return normalize(w1) == normalize(w2)


def get_anagrams(word, words):
    """Returns sorted list of anagrams of word in words"""
    return sorted(filter(ft.partial(is_eq, word), words))


def display(group):
    item = ', '.join(group)
    print(item)
    return item


def main(data):
    pdb.set_trace()

    # Create a unique list of sorted words
    groups = set(map(normalize, data))

    # Find anagrams of each unique word in the list of words
    anagrams = sorted(map(ft.partial(get_anagrams, words=data), groups))

    return anagrams


if __name__ == '__main__':
    data = [
       'pear',
       'amleth',
       'dormitory',
       'tinsel',
       'dirty room',
       'hamlet',
       'listen',
       'silnet',
    ]
    out = main(data)
    print('in:', data)
    print('out:')
    list(map(display, out))
