# %%
import numpy as np
import time
# %% prime factors

# check for primes
def check_factor(n, divisor):
    if n % divisor == 0:
        return True
    else:
        return False

def check_prime(n):
    counter = 2
    sqrt = np.sqrt(n)
    while counter <= sqrt:
        if n % counter == 0:
            return False
        counter += 1
    return True

def largest_prime_factor(n):
    sqrt = np.floor(np.sqrt(n))
    while True:
        if check_factor(n, sqrt) == True:
            if check_prime(sqrt) == True:
                largest_prime_factor = sqrt
                return largest_prime_factor
        sqrt -= 1

# %%
time1 = time.time()
print(largest_prime_factor(600851475143))
time2 = time.time()

print(f"Execution time: {time2 - time1}")

# %%
def biggest_prime_factor(n):
    i = 2
    while i**2 <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            print(f"n: {n}, i: {i}")
    return n

time1 = time.time()
print(biggest_prime_factor(600851475143))
time2 = time.time()

print(time2 - time1)