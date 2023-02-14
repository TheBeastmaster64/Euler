LIMIT = 1001
maximum = 0
p = 0
for i in range (0, LIMIT):
    ways = 0
    for j in range (0, i//2 + 1):
        for k in range (j, i):
            z = i - j - k
            if(z <= 0):
                break
            
            if(j*j + k*k == z*z):
                ways += 1




    if (ways > maximum):
        maximum = ways
        p = i

print(p)
