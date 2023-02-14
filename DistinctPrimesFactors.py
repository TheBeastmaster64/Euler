def get_primes(upper_limit):
    retval = [True for i in range(0, LIMIT+1)]
    retval[0] = False
    retval[1] = False
    for i in range (2, upper_limit+1):
        if(retval[i]):
            for j in range(i*i, upper_limit+1, i):
                retval[j] = False

    return retval

def get_factor_count(n, primes):
    retval = 0
    for i in range(2, n+1):
        if(primes[i] and n%i == 0):
            retval += 1

    return retval
            

LIMIT = 1000000
primes = get_primes(LIMIT)

value = -1
counter = 100

consecutive = 0
while(True):
    if(get_factor_count(counter, primes) == 4):
        consecutive += 1

        if(consecutive == 4):
            value = counter-3
            break
        if(consecutive == 2):
            print("2! ", counter)

        if(consecutive == 3):
            print("3! ", counter)
            
        counter += 1

    else:
        consecutive = 0
        counter += 1


    if(counter>LIMIT):
        break
print(value)
