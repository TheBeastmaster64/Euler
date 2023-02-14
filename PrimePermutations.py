def number_to_list(val):
    val = str(val)
    retval = []
    while(len(val) != 0):
        retval += [int(val[0])]
        val = val[1:]

    return retval


def check_if_permutation(list1, list2):
    if(len(list1) != len(list2)):
        return False

    while(len(list1) != 0 and len(list2) != 0):
        flag1 = True
        flag2 = False 
        for i in range (0, len(list1)):
            for j in range (0, len(list2)):
                if(list1[i] == list2[j]):
                    del list1[i]
                    del list2[j]
                    flag1 = False
                    break

                if(j == len(list2) - 1):
                    flag2 = True
                    flag1 = False
                    break
                
            if(flag1 == False):
                break
            
        if(flag2):
            break


    if(len(list1) == 0 and len(list2) == 0):
        return True
    
    return False
        

def get_primes(upper_limit):
    primes = [True for i in range (0, upper_limit+1)]
    primes[0] = False
    primes[1] = False
    for i in range (2, upper_limit+1):
        if(primes[i]):
            for j in range (i*i, upper_limit+1, i):
                primes[j] = False

    return primes

#ACTUAL CODE STARTS BELOW THIS POINT ---------------------------

LIMIT = 9999
primes = get_primes(LIMIT)

for i in range(1000, LIMIT+1):
    for j in range(2, (LIMIT-i)//2):
        if(not primes[i]):
            break
        
        else:
            if(not primes[i+j]):
                continue

            else:
                if(check_if_permutation(number_to_list(i), number_to_list(i+j))):
                    if(not primes[i+2*j]):
                        continue
                    
                    else:
                        if(check_if_permutation(number_to_list(i), number_to_list(i+2*j))):
                            print(i, ", ", i+j, ", ", i+2*j)

