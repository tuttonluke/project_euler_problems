#%%
# generate triangular numbers
# get list of divisors
import numpy as np
import matplotlib.pyplot as plt

def nth_triangular(n):
    num = 0
    for i in range(1, n+1):
        num += i
    return num

def get_divisors(n):
    divisors = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors

def count_divisors(n):
    no_divisors = 0
    # for every exact divisor up to the sqrt of n, there is 
    # a corresponding divisor above the sqrt.
    for i in range(1, int(np.sqrt(n))):
        if n % i == 0:
            no_divisors += 2
    return no_divisors

def first_triangular_with_n_divisors(n): # dumb algorithm
    num = 1
    iterations = 2
    nums = []
    divisors = []
    while True:
        n_divisors = len(get_divisors(num))
        print(f"{num} : {n_divisors}")
        nums.append(num)
        divisors.append(n_divisors)
        if n_divisors > n:
            return nums, divisors
        else:
            num += iterations
            iterations += 1

def plot_divisors(nums, divisors):
    plt.scatter(nums, divisors)

#%% Efficient algorithm

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
                print(num)
                count += 1
        return num

def prime_array(length_n):
    prime_array = np.array(2)
    if length_n == 1:
        return prime_array
    else:
        num = 1
        count = 1 # we know that 2 is a prime
        while count < length_n:
            num += 2
            if is_prime(num):
                prime_array = np.append(prime_array, num)
                count += 1
        return prime_array

def first_triangular_with_n_divisors_fast(n):
    num = 3 # start with a prime
    Dn = 2 # number of divisors for any prime
    count = 0 # ensure the while loop is entered
    array = prime_array(169) # generate primes up to first above 1000

    while count <= n:
        n = n + 1
        n1 = n
        if n1 % 2 == 0:
            n1 /= 2
        Dn1 = 1

        for i in range(1009):
            if array[i]**2 > n1:
                Dn1 *= 2
                break

            exponent = 1
            while n1 % array[i] == 0:
                exponent += 1
                n1 /= array[i]
            if exponent > 1:
                Dn1 *= exponent
            if n1 == 1:
                break
        count = Dn*Dn1
        print(count)
        Dn = Dn1
    print((num * (num-1)) / 2)

# %%
if __name__ == "__main__":
    first_triangular_with_n_divisors_fast(500)