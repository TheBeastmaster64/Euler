from itertools import permutations


def is_valid(tup):
    if(tup[0] == 0):
        return False
    return True


def tuple_to_str(tup):
    retval = ""
    for i in range(0, len(tup)):
        retval = retval + str(tup[i])
    return retval


def fits_property(val, primes):
    for i in range(1, len(val)-2):
        thing = int(val[i:(i+3)])
        if(thing % primes[i-1] != 0):
            
            return False

    return True

        
primes = [2, 3, 5, 7, 11, 13, 17]

perm_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(permutations(perm_list))
alt_list = []
for i in range(0, len(perms)):
    if(is_valid(perms[i])):
        alt_list.append(tuple_to_str(perms[i]))

summation = 0

for i in range(0, len(alt_list)):
    if(fits_property(alt_list[i], primes)):
        summation += int(alt_list[i])


print(summation)
