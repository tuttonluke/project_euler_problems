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




# %%
if __name__ == "__main__":
    nums, divisors = first_triangular_with_n_divisors(50)
    plot_divisors(nums, divisors)