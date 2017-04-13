import functools as ft
import operator as op


def normalize(x):
    return x.replace('.', '').replace(',', '').lower()


def is_int(x):
    return True if x.isdigit() else False


def not_int(x):
    return True if not x.isdigit() else False


def is_hotel(id, score):
    return True if id == score[0] else False


def in_hotlist(w, kwords):
    return True if normalize(w) in kwords else False


def get_score(review, kwords):
    hot = list(filter(ft.partial(in_hotlist, kwords=kwords), review[1].split()))
    score = ft.reduce(op.add, (1 for _ in hot), 0)
    return review[0], score


def count_score(x, y):
    score = x[1] + y[1]
    return x[0], score


def by_value(x):
    return x[1]


def main(data):
    kwords = list(map(normalize, data[0].split()))
    reviews = data[2:]
    h_ids = list(filter(is_int, reviews))

    pairs = zip(
        h_ids,
        filter(not_int, reviews)
    )

    scores = list(map(ft.partial(get_score, kwords=kwords), pairs))

    totals = {x: ft.reduce(count_score,
                           filter(ft.partial(is_hotel, x), scores))[1]
              for x in h_ids}

    return sorted(totals.items(), key=by_value, reverse=True)


if __name__ == '__main__':
    data = [
        'breakfast beach citycenter location metro view staff price',
        '5',

        '1',
        'This hotel has a nice view of the citycenter. The location is perfect.',

        '2',
        ('The breakfast is ok. Regarding location, it is quite far from '
         'citycenter but price is cheap so it is worth it.'),

        '1',
        ('Location is excellent, 5 minutes from citycenter. There is alse a metro '
         'station very close to the hotel.'),

        '1',
        ("They said I couldn't take my dog and there were other guests with "
         "dogs! That is not fair."),

        '2',
        ('Very friendly staff and good cost-benefit ratio. Its location is a '
         'bit far from citycenter.'),
    ]
    out = main(data)
    print('in:', data, '\n')
    print('out:', *[x[0] for x in out])
