import functools as ft


"""
ft.reduce(func, iter[, init])
"""
def add(n, b=0):
    return n + b

numbers = [
    5,  # 5 + 0
    6,  # 6 + 5
    8,  # 8 + x
]

result = ft.reduce(add, numbers)
print(result)


"""
ft.partial(func, *args, **kwargs)
"""
