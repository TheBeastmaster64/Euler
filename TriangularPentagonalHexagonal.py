import math

def is_hexagon(x):
    val = int(math.sqrt(8*x + 1))
    if(8*x + 1 == val*val and val % 4 == 3):
        return True
    return False

"""
def is_pentagon(x):
    val = int(math.sqrt(24*x + 1))
    if(24*x + 1 == val*val and val % 6 == 5):
        return True
    return False
"""


#LIMIT = 1000000000
COUNT_MAX = 5
count = 0
i = 1
while(count < COUNT_MAX):
    val = i*(3*i-1)//2
    if(is_hexagon(val)):
        print(val)
        count += 1

    i += 1




