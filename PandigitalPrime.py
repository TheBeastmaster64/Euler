import itertools


LIMIT = 10000001

def tuple_to_int(tup):
    retval = 0
    for i in range(len(tup)-1, -1, -1):
        retval *= 10
        retval += tup[i]
        
    return retval

    
def get_primes(upper_limit):
    primes = [True for i in range (upper_limit + 1)]
    primes[0] = False
    primes[1] = False
    for i in range (2, upper_limit + 1):
        if(primes[i] == True):
            for j in range (i*i, upper_limit+1, i):
                primes[j] = False

    return primes



max_found = 0
primes = get_primes(LIMIT)

for i in range (7, 0, -1):
    current_list = []
    for j in range (1, i+1):
        current_list.append(j)

    perms = list(itertools.permutations(current_list))
    for j in range(0, len(perms)):
        perms[j] = tuple_to_int(perms[j])
        if(primes[perms[j]] and perms[j] > max_found):
            max_found = perms[j]

    if(max_found > 0):
        break

print(max_found)

