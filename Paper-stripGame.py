nim_vals = [0, 0, 1]
for i in range(3, 10000, 2):
    arr = []
    record = []
    for k in range(0, 100): #100 is an arbitrary number here
        record.append(False)
        
    for j in range(0, i-1): # Goes until i-2 
        val = nim_vals[j] ^ nim_vals[i-2-j]
        record[val] = True
        arr.append(val)

    count = 0
    while(record[count]):
        count += 1
        
    nim_vals.append(count)

count = 0 
for i in range(1, len(nim_vals)):
    if(nim_vals[i] == 0):
        count += 1

print(count)
