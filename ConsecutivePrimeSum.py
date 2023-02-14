def arr_to_list(arr):
    retval = []
    for i in range(0, len(arr)):
        if(arr[i]):
            retval.append(i)

    return retval


def get_primes(upper_limit):
    primes = [True for i in range(0, upper_limit+1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, upper_limit+1):
        if(primes[i]):
            for j in range(i*i, upper_limit+1, i):
                primes[j] = False

    return primes

#ACTUAL PROGRAM STARTS HERE -------------------

LIMIT = 999999
primes = get_primes(LIMIT)
prime_list = arr_to_list(primes)
cons_sum_list = []

print(len(prime_list))
for i in range(0, len(prime_list)//20):
    cons_num = 0
    summation = 0
    for j in range(0, len(prime_list)//20 - i):
        summation += prime_list[i+j]
        cons_num += 1

        cons_sum_list.append([summation, cons_num])
        
cons_sum_list.sort

max_val = 0
num_at_max_val = 0
for i in range(0, len(cons_sum_list)):
    if(cons_sum_list[i][0] > len(primes) - 1):
        continue
    
    if(primes[cons_sum_list[i][0]]):
        if(cons_sum_list[i][1] > max_val):
            max_val = cons_sum_list[i][1]
            num_at_max_val = cons_sum_list[i][0]


print(num_at_max_val)
