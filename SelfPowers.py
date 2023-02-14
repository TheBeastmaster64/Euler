def ten_power(num, val, mod):
    retval = 1
    while(val > 0):
        retval *= num
        retval = retval % mod
        val -= 1

    return retval

MOD = 10000000000
LIMIT = 1000
summation = 0
for i in range (1, LIMIT+1):
    summation += ten_power(i, i, MOD)
    summation = summation % MOD

print(summation)
