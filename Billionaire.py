def factorial(n):
    if(n==0):
        return 1

    return n*factorial(n-1)


#CODE STARTS HERE
    
LIMIT = 1000000000
MAX = 568

summation = 0
for i in range (0, MAX+1):
    summation += factorial(1000)/(factorial(i)*factorial(1000-i))


print(summation/pow(2, 1000))
