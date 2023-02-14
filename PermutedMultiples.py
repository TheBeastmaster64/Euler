def check_all(v1):
    arr = []
    for i in range(1, 7): 
        arr.append(str(i*v1))
    return sorted(arr[0]) == sorted(arr[1]) == sorted(arr[2]) == sorted(arr[3]) == sorted(arr[4]) == sorted(arr[5])
    
LIMIT = 10000000
for i in range(0, LIMIT):
    if(check_all(i)):
        print(i)
