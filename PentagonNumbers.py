import math

def is_pentagonal(x):
    val = int(math.sqrt(24*x + 1))
    if(24*x + 1 == val*val and val % 6 == 5):
        return True

    return False


def does_contain(val, my_list, lower_limit, upper_limit):
    mid = (upper_limit + lower_limit) // 2
    comp_val = my_list[mid] 
    if(val == comp_val):
        return True

    elif(lower_limit == upper_limit):
        return False
    
    elif(val < comp_val):
        return does_contain(val, my_list, lower_limit, mid)

    elif(val > comp_val):
        return does_contain(val, my_list, mid+1, upper_limit)

    
LIMIT = 10000
nums = []
for i in range(1, LIMIT+1):
    nums.append(int(i*(3*i-1)/2))


flag = False
for i in range(0, LIMIT):
    for j in range(i+1, LIMIT):
        if(is_pentagonal(nums[j]-nums[i]) and is_pentagonal(nums[j]+nums[i])):
            print(nums[i])
            print(nums[j])
            print(nums[j]-nums[i])
            flag = True
            break
            

    if(flag):
        break

