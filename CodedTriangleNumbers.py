import math

def is_triangular(val):
    alt = int(math.sqrt(8*val+1))
    if(8*val+1 == alt*alt):
        return True
    return False


file = open("../Files/WordTriangularNumber.txt")
char_list = list(file.read())
summation = 0
count = 0
for i in range (0, len(char_list)):
    if(char_list[i] == '"'):
        continue

    if(char_list[i] == ','):
        if(is_triangular(summation)):
            count += 1
        summation = 0
        continue
    
    summation += ord(char_list[i]) - 64

    
print(count)
