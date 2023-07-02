#%%
import numpy as np
import time

def Collatz_length(n):
    sequence = []
    while n > 1:
        if n % 2 == 0:
            n //= 2
            sequence.append(n)
        else:
            n = 3*n + 1
            sequence.append(n)
    return len(sequence)

"""
1)
C(10) = C(5) + 1, so don't need to calculate
the whole chain of C(10) if you store the length of C(5).

2) 
C(2n) > C(n), so only need to consider values > upper_bound / 2.

3) 
If n is odd, then 3n + 1 is even, hence: n -> 3n + 1 -> (3n + 1)/2.
A step is saved by C(n) = C((3n + 1)/2 + 2)
"""

def longest_Collatz_fast(limit):

    calculated = {n: 0 for n in range(1, limit + 1)}
    # initial values
    calculated[1] = 1
    calculated[2] = 2

    for n in range(limit//2, limit + 1):
        counter = 0
        current = n

        while n > 1:
            if n < current:
                calculated[current] = calculated[n] + counter
                break
            if n % 2 == 0:
                n = n / 2
                counter += 1
            else:
                n = (3*n + 1) / 2
                counter += 2

    return list(calculated.values()).index(max(calculated.values())) + 1

start = time.time()
value = longest_Collatz_fast(1000000)
stop = time.time()

print(value)
print(stop - start)



