import functools as ft
import operator as op
import itertools as it


def get_next(base, pair):
    return pair if (pair[0] - base[0]) == 1 else None


def pick_pair(base, pairs):
    find = tuple(filter(ft.partial(get_next, base), pairs))
    find = find[0] if find else None
    return (find[1], base[1]) if find else None


def get_delta(n1, n2):
    delta = n1 - n2
    return (-128, delta) if not (-127 <= delta <= 127) else (delta,)


def format_delta(x):
    return ' '.join(map(str, x))


def main(data):
    data = list(map(int, data.split()))
    bases = enumerate(data)
    pairs = list(enumerate(data))
    base_pairs = filter(
        op.truth,
        map(ft.partial(pick_pair, pairs=pairs), bases)
    )
    deltas = [str(data[0])]
    deltas = deltas + list(map(
        format_delta,
        it.starmap(get_delta, base_pairs)
    ))
    return deltas


if __name__ == '__main__':
    data = '25626 25757 24367 24267 16 100 2 7277'
    out = main(data)
    print('in:', data, '\n')
    print('out:', *out)
