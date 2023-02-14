def get_primes(upper_limit):
    retval = [True for i in range(0, LIMIT+1)]
    retval[0] = False
    retval[1] = False
    for i in range (2, upper_limit+1):
        if(retval[i]):
            for j in range(i*i, upper_limit+1, i):
                retval[j] = False

    return retval


LIMIT = 1000000
primes = get_primes(LIMIT)

val = -1
counter = 3
flag = False
while(True):
    if(primes[counter]):
        counter += 2
        continue

    
    test = 1
    while(not primes[counter - 2*test*test]):  
        if(counter - 2*test*test <= 1):
            val = counter
            flag = True
            break
        
        test += 1

        
    if(flag):
        break

    counter += 2


print(counter)
