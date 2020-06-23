"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def add_my_multiples(y: int):
    my_total = 0
    for x in range(1, int(999/y) + 1):
        my_total += y * x
    return my_total

total = 0
total += add_my_multiples(3)
total += add_my_multiples(5)
total -= add_my_multiples(15)
print (total)
