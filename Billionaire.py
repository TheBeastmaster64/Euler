"""
class Node:
    def __init__(self):
        self.value = None
        self.right_child = None
        self.left_child = None

    def is_leaf(self):
        if(self.right_child == None and self.left_child == None):
            return True
        return False
        
    def set_value(self, value):
        self.value = value
    
    def set_right(self, right):
        self.right_child = right

    def set_left(self, left):
        self.left_child = left

    def get_value(self):
        return self.value
    
    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child




def simulate(i, current_node, value, proportion):
    current_node.set_value(value)
    if(i == 0):
        return
    
    current_node.set_right(Node())
    current_node.set_left(Node())

    simulate(i-1, current_node.get_right(), 2*value*proportion+value, proportion)
    simulate(i-1, current_node.get_left(), value - proportion*value, proportion)


SIZE_LIMIT = 2
def print_tree_and_get_chance(root):
    if(root == None):
        return -1

    stack = []
    stack.append(root)
    count = 0
    while(len(stack) != 0):
        node = stack.pop()
        if(node.get_left() != None):
            stack.append(node.get_right())
            
        if(node.get_right() != None):
            stack.append(node.get_left())

        if(node.is_leaf()):
            print("{0:.2f}".format(node.get_value()), end = " ")
            if(node.get_value() >= SIZE_LIMIT):
                count += 1

    return count
    
    
"""
def factorial(n):
    if(n==0):
        return 1

    return n*factorial(n-1)


#CODE STARTS HERE
    
LIMIT = 1000000000
MAX = 568
#root = Node()
#root.set_value(1)
#n = LIMIT
"""
for i in range(0, 101):
    proportion = i/100
    simulate(n, root, 1, proportion)
    count = print_tree_and_get_chance(root)
    print("For proportion ", proportion, ":", end = " ")
    print("Chance: ", (count/pow(2, LIMIT)))
    print()
"""
"""
maximum = 550
ideal_x = 0
for i in range(550, 600):
    x = (2000-3*i)/2000
    value = pow(1-x, i)*pow(1+2*x, 1000-i)
    if(value >= LIMIT):
        maximum = i
        ideal_x = x

print(maximum, " ", ideal_x)
"""
summation = 0
for i in range (0, MAX+1):
    summation += factorial(1000)/(factorial(i)*factorial(1000-i))


print(summation/pow(2, 1000))
