def get_largest_pow(base, val):
    largest_pow = 1
    while(val//largest_pow > 0):
        largest_pow *= base

    return largest_pow//base


def ten_to(x):
    retval = 1
    for i in range (0, x):
        retval *= 10

    return retval


def is_palindrome(x):
    if(len(x) < 2):
        return True

    first_value = x[0]
    second_value = x[-1]
    if(first_value == second_value):
        return is_palindrome(x[1:-1])

    else:
        return False


def base_10_to_2(val):
    largest_pow = get_largest_pow(2, val)
    retval = 0
    while(largest_pow > 0):
        retval *= 10
        retval += val//largest_pow
        val = val - (val//largest_pow)*largest_pow
        largest_pow = largest_pow//2

    return retval

"""
def reverse(val):
    largest_pow = get_largest_pow(10, val)
    retval = 0
    while(largest_pow > 0):
        retval += val%10 * largest_pow
        val = val//10
        largest_pow = largest_pow//10

    return retval
"""

"""
ten_power = 1
total = 0
digit_count = 1
for i in range(1, 1000):
    if(i/(ten_power*10) == 1):
        ten_power *= 10
        digit_count += 1
        
    if(i%2 != 0):
        pal = str(i)
        pal = pal[::-1] + pal
        pal_conj = base_10_to_2(int(pal))
        if(is_palindrome(str(pal_conj))):
            total += int(pal)

        pal = str(i)
        pal = pal[1:][::-1] + pal
        pal_conj = base_10_to_2(int(pal))
        if(is_palindrome(str(pal_conj))):
            total += int(pal)
"""

total = 0
for i in range(0, 1000000):
    if(is_palindrome(str(i))):
        pal_conj = base_10_to_2(int(i))
        if(is_palindrome(str(pal_conj))):
            total += i

print(total)

    







        
