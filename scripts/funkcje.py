from functools import partial

def division(x, y):
    return x/y

divide_by_two = partial(division,2)

print(divide_by_two(6))
print(divide_by_two(11))
print(divide_by_two(7))