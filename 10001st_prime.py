#%%
import numpy as np

def is_prime(n):
    if n == 1:
        return False
    elif n < 4: # 2 & 3 are primes
        return True
    elif n % 2 == 0: # All primes > 2 are odd.
        return False
    elif n < 9: # 5 & 7 are primes
        return True
    elif n % 3 == 0:
        return False
    else:
        r = np.floor(np.sqrt(n)) # rounded to largest integer such that r x r < n
        f = 5 # already excluded multiples of 2 & 3
        while f < r + 1:
            if n % f == 0:
                return False
            elif n % (f+2) == 0: # no point checking f+1 because it will be even
                return False
            f += 6 # all primes > 3 can be written in the form 6k +/- 1
        return True # in all other cases

def nth_prime(n):
    if n == 1:
        return 2
    else:
        num = 1
        count = 1 # we know that 2 is a prime
        while count < n:
            num += 2
            if is_prime(num):
                count += 1
        return num
# %%
if __name__ == "__main__":
    for i in range(1, 30):
        print(nth_prime(i))