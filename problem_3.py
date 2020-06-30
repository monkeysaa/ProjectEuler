"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

product = 600851475143
root = math.sqrt(product)
root = int(root)

# This function finds all factors of a number
# Checks values between x and square root and returns all factors and their partners in a set.
# For-loop limited to the product's square root for efficiency, adding factor and its multiplicative partner to list.

def find_factors(product):
    factors = []
    x = 0
    
    for x in range (1, root + 1):
        if product % x == 0:
            factors += [x, product // x]
    
    factors.sort()
    
    print("The factors of", product, "are:")        
    print (factors)
    return factors

# create factors list 
factors = find_factors(product)
# remove 1 for simplicity
factors.remove(1)

# creates identical list prime_factors, from factors
prime_factors = list(factors)

# loop through all elements in prime_factors
# checks against factors to remove composites from prime_factors list
for i in prime_factors:
    for t in factors:
        print("i is", i, ". t is", t)
        # don't remove identicals (eg. 13 is divisible by 13)
        if t == i:
            continue
        
        # if t is composite, remove from prime_factors
        elif t % i == 0:
            if (t in prime_factors):
                prime_factors.remove(t)

print("The prime factors are: ", prime_factors)