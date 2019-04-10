## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    import math
    if x <= 1: 
        return x
    if x == 2:
        return 1
    goal = int(x/2)

    while goal**2 > x:
        goal = int(goal/2)
    up = goal * 2
    low = goal

    while up - low > 1:
        if ((up + low)/2) **2 <= x:
            low = math.floor((up + low)/2)
        else:
            up = math.ceil((up + low)/2)
    if up ** 2 <= x:
        return up
    return low


################# Question 2 #################

'''
x_0: initial guess
EPSILON: stop when abs(x - x_new) < EPSILON
MAX_ITER: maximum number of iterations

NOTE: you must use the default values of the above parameters, do not change them
'''
def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    timer = MAX_ITER
    x = x_0
    while timer:
        timer -= 1
        x_1 = x
        x = x - f(x)/fprime(x)
        if abs(x - x_1) <= EPSILON:
            return x
    return x


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    tree = Tree(tokens[0])
    parent = tree
    child = tree
    ancester = []
    have_add = False
    i = 1
    while i < len(tokens):
        if tokens[i] == '[':
            ancester.append(parent)
            parent = child
            i += 1
            continue

        if tokens[i] == ']':
            i += 1
            parent = ancester.pop()
            continue
            
        child = Tree(tokens[i])
        parent.add_child(child)
        i += 1   
    return tree

def max_depth(root): # do not change the heading of the function
    if root.children == None:
        return 1
    result = [1]
    for i in root.children:
        result.append(max_depth(i)+1)
    return max(result)
