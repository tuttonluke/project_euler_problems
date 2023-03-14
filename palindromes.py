# %%
def check_palindrome(n):
    """Doesn't work for <4 digit numbers.
    """
    num_string = str(n)
    if len(num_string) % 2 == 0:
        for i in range(len(num_string) // 2):
            if num_string[i] != num_string[-i - 1]:
                return False
    
    else:
        for i in range(len(num_string) // 2 - 1):
            if num_string[i] != num_string[-i - 1]:
                return False

    return True


def largest_palindrome(no_digits):
    n = 10**no_digits - 1
    largest_pal = 0
    
    for i in range(n, 1, -1):
        for j in range(n, 1, -1):
            product = i * j
            if check_palindrome(product) == True and product > largest_pal:
                largest_pal = product
                print(f"{i} x {j} = {product}")
    return largest_pal
            
largest_palindrome(4)

# %%