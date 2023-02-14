from itertools import count, filterfalse # ifilterfalse on py2



"""
def split(my_list, i, j):
    num_copy = my_list.copy()
    num_copy.extend([my_list[i]-2-j, j])
    num_copy.pop(i)
    return num_copy

    

def get_type(num, key):
    summation = 0
    flag = False
    for i in range(0, len(num)):
        if(num[i]>len(key)-1):
            flag = True
            break
        summation += key[num[i]]

    if(summation == 0 and not flag):
        return 0

    elif(summation == 1 and not flag):
        return 1

    else:
        for i in range(0, len(num)):
            for j in range(0, num[i]-2+1):
                if(num[i]-2-j >= 0):
                    if(get_type(split(num, i, j), key) == 0):
                        return 1

    return 0
        




key = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]


print(get_type([35], key))
"""
#x = 1
#count = 0
#is_four = 0
#mod = 4
#while(x <= 1000000):
#    if(is_four < mod//2):
#        x += 4
#        is_four += 1
#        count += 1
#
#    else:
#        x += 6
#        is_four += 1
#        count += 1
#
#    if(is_four%mod == 0):
#        is_four = is_four%mod
#        mod = mod + 2

#print(count)


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
