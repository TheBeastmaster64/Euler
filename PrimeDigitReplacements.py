def count_primes_in_set(primes, val, add_val, digit, ): #primes is the prime array. val is the first prime. add_val is the value added each time. digit is the start value of the repeat digit. LIMIT is upper limit
    counter = 1
    while digit < 10: #We do not want a carry
        val+=add_val
        if(val >= len(primes)):
            break
        
        if(primes[val]):
            counter += 1
        digit += 1

    return counter


def get_three_repeat(p):
    counts = []
    for i in range(0, 10): #number of digits
        counts.append(0)

    digit = 0
    loop_count= 0
    while(p != 0):
        digit = p%10
        p = p//10
        counts[digit] += 1
        loop_count += 1

    for i in range(0, len(counts)):
        if(counts[i] == 3):
            return i #if a 3-rep exists, it is returned. Else -1 is returned
    return -1


def get_adder(p, repeat_digit):
    add_val = 0 #value which sould be added
    p = str(p)
    for i in range(0, len(p)):
        add_val *= 10
        if(int(p[i]) == repeat_digit):
            add_val += 1

    return add_val


def get_primes(LIMIT):
    primes = [False, False]
    for i in range(2, LIMIT):
        primes.append(True)
    for i in range(2, len(primes)):
        if(primes[i]):
            for j in range(i*i, len(primes), i):
                primes[j] = False

    return primes


#PROGRAM STARTS HERE
START_INDEX = 100000 #Starts here since it is unlikely there is a 3-repeat under 100k
LIMIT = 10000000
primes = get_primes(LIMIT)

for i in range(START_INDEX, len(primes)):
    if(primes[i]):
        val = get_three_repeat(i)
        if(val != -1 and (val == 0 or val == 1 or val == 2)):
            adder = get_adder(i, val)
            if(count_primes_in_set(primes, i, adder, val) == 8):
                print(i)
