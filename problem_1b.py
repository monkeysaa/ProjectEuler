"""
Find the sum of all the multiples of 3 or 5 below 1000.

Approach 2

For x = 0 through x = 1000,
    Run through each number.
    Check if multiple of var1 (using mod var1)
        if yes —> add 
        else —> Check if multiple of var2 (using mod var2)
            if yes --> add 
            else --> Pass

Generalize by making function (var1, var2, cap)
"""
def sum_multiples(var1, var2, cap):
    subtotal = 0
    for i in range(cap):
        if i % var1 == 0:
            subtotal += i
        elif i % var2 == 0:
            subtotal += i
    return subtotal

print(sum_multiples(3, 5, 1000))
