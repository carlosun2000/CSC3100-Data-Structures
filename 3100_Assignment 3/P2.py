class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

class BST:
    def __init__(self,initialist):
        self.root = None
        self.construct_bst(initialist)

    def construct_bst(self, initiallist):
        for i in initiallist:
            tmp=Node()
            tmp.value=i
            self.insert(tmp)

    def insert(self, z:Node):
        y = None
        x = self.root
        while (not (x is None)):
            y=x
            if z.value<x.value:
                x=x.left
            else:
                x=x.right
        z.parent = y
        if (y is None):
            self.root = z
        else:
            if z.value<y.value:
                y.left = z
            else:
                y.right = z
    
    def findmin(self,node:Node):
        curr = node
        while not (curr.left is None):
            curr = curr.left
        return curr
    
    def findmax(self,node:Node):
        curr = node
        while not (curr.right is None):
            curr = curr.right
        return curr
    
    def successor(self,node:Node):
        if not (node.right is None):
            return self.findmin(node)
        y = node.parent
        while(not (y is None) and node == y.right):
            node = y
            y=y.parent
        return y
    
    def predecessor(self,node:Node):
        if not (node.left is None):
            return self.findmax(node)
        y = node.parent
        while(not (y is None) and node == y.left):
            node = y
            y=y.parent
        return y


class Price_Manager():
    def __init__(self,initialist) :
        self.top = initialist[-1]
        self.bst=BST(initialist)
        self.size = len(initialist)
        tmp = sorted(initialist)

        self.adj_min = float("inf")

        for i in range(self.size-1):
            self.adj_min = min(self.adj_min , abs(initialist[i]-initialist[i+1]))

        self.all_min = float("inf")

        for i in range(self.size-1):
            self.all_min = min(self.all_min , abs(tmp[i]-tmp[i+1]))

    def add_value(self,value):
        self.adj_min=min(abs(self.top-value),self.adj_min)
        self.top = value

        z = Node()
        z.value = value
        self.bst.insert(z)
        s = self.bst.successor(z)
        p = self.bst.predecessor(z)
        if (s is None):
            diff = abs(p.value-z.value)
        elif (p is None):
            diff = abs(s.value-z.value)
        else:
            diff = min(abs(s.value-z.value),abs(p.value-z.value))
        self.all_min = min(self.all_min , diff)

    def conduct_instruction(self,instruction):
        if instruction == "CLOSEST_ADJ_PRICE":
            print(self.adj_min)
        elif instruction == "CLOSEST_PRICE":
            print(self.all_min)
        else:
            self.add_value(int(instruction[4:]))


n,m = map(int,input().split())
initial_sequence = list(map(int,input().split()))
pm = Price_Manager(initial_sequence)
for _ in range(m):
    instruction = input()
    pm.conduct_instruction(instruction)
    
    



