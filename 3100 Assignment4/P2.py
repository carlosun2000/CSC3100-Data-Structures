class Queue:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return len(self.array) == 0

    def enqueue(self, item):
        self.array.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.array.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def size(self):
        return len(self.array)
    
class Node:
    def __init__(self):
        self.neighbor_index = list()
        self.value = -1
        self.color = 0

class Graph:
    def __init__(self,n_vertex):
        #initialize the graph so that index i is the node with value i+1 in the array
        self.array = [None]
        for i in range(1,n_vertex+1):
            n = Node()
            n.value = i
            self.array.append(n)

    def add_pair(self,a,b):
        if b not in self.array[a].neighbor_index:
            posa = 0
            lena = len(self.array[a].neighbor_index)
            while posa < lena and self.array[a].neighbor_index[posa] < b:
                posa += 1
            self.array[a].neighbor_index.insert(posa, b)
            posb = 0
            lenb = len(self.array[b].neighbor_index)
            while posb < lenb and self.array[b].neighbor_index[posb] < a:
                posb += 1
            self.array[b].neighbor_index.insert(posb, a)

    def bfs(self,s):
        
        Q = Queue()
        start_node = self.array[s]
        Q.enqueue(start_node)
        start_node.color = 1
        while not Q.is_empty():
            v = Q.dequeue()
            for index in v.neighbor_index:
                sub_node = self.array[index]
                if sub_node.color ==0:
                    Q.enqueue(sub_node)
                    sub_node.color = 1
            v.color = 2
            print(v.value, end=" ")
            


    def bfs_edge_add(self,s,k):
        Q = Queue()
        start_node = self.array[s]
        Q.enqueue(start_node)
        start_node.color = 1
        while not Q.is_empty():
            v = Q.dequeue()
            children = v.neighbor_index
            eligible_list = find_pairs_ordered(children,k)
            for pair in eligible_list:
                a,b = pair
                if a!=b:
                    self.add_pair(a,b)
            for index in children:
                sub_node = self.array[index]
                if sub_node.color ==0:
                    Q.enqueue(sub_node)
                    sub_node.color = 1
            v.color = 2

    def clear_color(self):
        for index in range(1,len(self.array)):
            node = self.array[index]
            node.color=0

def find_pairs_ordered(lst, k):
    result = []
    i, j = 0, 1
    while j < len(lst):
        u, v = lst[i], lst[j]
        if u == k * v or v == k * u:
            result.append((u, v))
        if v <= k * u:
            j += 1
        else:
            i += 1
    return result

n,m,k,s = map(int,input().split())
G=Graph(n)
for i in range(m):
    a,b = map(int,input().split())
    G.add_pair(a,b)


G.bfs_edge_add(1,k)
G.clear_color()
G.bfs(s)