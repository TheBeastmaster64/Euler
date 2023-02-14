LIMIT = 1000000
"""
def truncate_right(val):
    while(val != 0):
        if(!primes[val]):
            return False
        val //= 10
        
    return True
"""

def is_trunctable_left(val, ten_pow, primes):
    while(val != 0):
        if(not primes[val]):
            return False
        val = val % ten_pow
        ten_pow //= 10

    return True

    
def get_primes(upper_limit):
    primes = [True for i in range(upper_limit+1)]
    primes[1] = False
    primes[0] = False
    for i in range (2, upper_limit+1):
        if(primes[i]):
            for j in range (i*i, upper_limit+1, i):
                primes[j] = False

    return primes

truncs = []
def add_trunc_primes(p, primes, ten_pow):
    global truncs
    if(p > LIMIT):
        return 0
    
    if(primes[p]):
        if(ten_pow > 1 and is_trunctable_left(p, ten_pow, primes)):
            truncs.append(p)
            return p + add_trunc_primes(p*10 + 1, primes, ten_pow*10) + add_trunc_primes(p*10 + 3, primes, ten_pow*10) + add_trunc_primes(p*10 + 7, primes, ten_pow*10) + add_trunc_primes(p*10 + 9, primes, ten_pow*10)
        else:
            return add_trunc_primes(p*10 + 1, primes, ten_pow*10) + add_trunc_primes(p*10 + 3, primes, ten_pow*10) + add_trunc_primes(p*10 + 7, primes, ten_pow*10) + add_trunc_primes(p*10 + 9, primes, ten_pow*10)

    return 0

    
primes = get_primes(LIMIT)
summation = 0

for i in range(0, 10):
    if(primes[i]):
        summation += add_trunc_primes(i, primes, 1)

"""
while(count < 11 and i < LIMIT + 1):
    if(i//(ten_pow*10) > 0):
        ten_pow *= 10
        
    flag = False
    if(primes[i]):
        val = i
        while(primes[val]):
            val = truncate_right(val)
        if(val == 0):
                flag = True
        
        if(flag):
            flag = False
            val = i
            modify_val = ten_pow
            while(primes[val]):
                val = truncate_left(val, modify_val)
                modify_val = modify_val//10
                
            if(val == 0):
                flag = True
                
        if(flag):
            truncs.append(i)
            count += 1
            summation += i 

    i += 1
"""    
    
print(truncs)
print(summation)
