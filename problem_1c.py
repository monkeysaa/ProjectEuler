from typing import Set 

"""
Find all multiples of 3 and 5, toss out duplicates
Sets - only add each value once (remove duplicates)

This is not the most efficient way to solve this problem,
but good practice with lists and sets. 
"""

def find_my_multiples(y: int, cap: int):
    multiples = set()
    x = y
    while x < cap:
        multiples.add(x)
        x += y 
    return multiples

all_multiples: Set[int] = set()

all_multiples.update(find_my_multiples(3, 1000))
all_multiples.update(find_my_multiples(5, 1000))

total = 0
for x in all_multiples:
    total += x

print (total)