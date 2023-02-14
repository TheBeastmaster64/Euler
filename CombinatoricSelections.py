def choose(i,j):
    return factorial(i)/(factorial(j)*factorial(i-j))
    
def factorial(n):
    if(n == 0):
        return 1
    return n*factorial(n-1)

count = 0
LIMIT = 1000000
for i in range(23, 101):
    for j in range(3, i):
        if(choose(i,j) >= LIMIT):
            count += 1

print(count)
