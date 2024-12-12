import sys
sys.setrecursionlimit(2000000)
class TreeNode:
    def __init__(self, color):
        self.color = color
        self.next = dict()

class Graph:
    def __init__(self,color_list):
        self.sub_black = dict()
        self.sub_b = dict()
        self.count = dict()
        self.size = len(color_list)
        self.base = [None]*100000+[None]
        for i in range(len(color_list)):
            color = color_list[i]
            self.base[i+1] = TreeNode(color)
            self.sub_black[self.base[i+1]] = []
            self.sub_b[self.base[i+1]] = 0
            self.count[self.base[i+1]] = 0


    def insert(self, start,end,length):
        start_node:TreeNode = self.base[start]
        end_node:TreeNode = self.base[end]
        start_node.next[end_node] = length
    
    def next_black_dis(self,start:TreeNode):
        dis = []
        
        for child in start.next.keys():
            length = start.next[child]
            
            if child.color == 1:
                dis.append(length)
            k= [i+length for i in self.next_black_dis(child)]
            dis+=k

            tmp = []
            length = start.next[child]
            
            if child.color == 1:
                tmp.append(length)
            tmp += k
            t = (sum(tmp),len(tmp))
            self.sub_black[start].append(t)

        return dis
    
    def countnum_black(self,start:TreeNode):
        count = 0
        for child in start.next.keys():
            pass
        if (len(start.next)>0):
            if child.color==1:
                count+=1
            count+=self.countnum_black(child)
        self.count[start]=count
        return count

    
    def sum_distance_black(self,start:TreeNode):
        total_sum = 0
        count = self.count[start]

        for child in start.next.keys():
            length = start.next[child]
        
        if (len(start.next)>0):   
            total_sum+=length*count + self.sum_distance_black(child)
        self.sub_b[start]=total_sum
        return total_sum
    
    def listwise(self,start:TreeNode):
        distance = 0
        if start.color == 1:
            distance += self.sub_b[start]
        for child in start.next.keys():
            pass
        if (len(start.next)>0): 
            distance += self.listwise(child)
            
        return distance

    def dfs(self,start:TreeNode):
        distance = 0

        #Exclusion
        for child in start.next.keys():
            tmp = self.dfs(child)
            distance += tmp
        
        #Inclusion
        array = self.sub_black[start]
        distance += sum_of_sum_of_pairs_optimized(array)
        if start.color ==1:
            distance+=sum_of_tuple(array)

        return distance
    
def sum_arrays(a1,a2):
    sum=0
    for i in a1:
        for j in a2:
            sum+=i+j
    return sum

def sum_of_sum_of_pairs_optimized(tuples_list):
    total_sum = 0
    running_value_sum = 0
    running_anti_count_sum = 0

    for value, anti_count in tuples_list:
        total_sum += (value * running_anti_count_sum) + (anti_count * running_value_sum)
        running_value_sum += value
        running_anti_count_sum += anti_count
    
    return total_sum

def sum_of_tuple(tuples_list):
    total_sum = 0
    for v,_ in tuples_list:
        total_sum +=v
    return total_sum




# color_list=[0,1,0,1,1]

# graph = Graph(color_list)
# graph.insert(1,2,1)
# graph.insert(2,3,2)
# graph.insert(3,4,2)
# graph.insert(4,5,1)


# graph.countnum_black(graph.base[1])
# graph.sum_distance_black(graph.base[1])
# print(graph.count)
# print(graph.sub_b)
# print(graph.listwise(graph.base[1]))



n = int(input())
color_list = list(map(int,input().split()))
graph = Graph(color_list)
flag = True
for end in range(2,n+1):
    start,length = map(int,input().split())
    if flag:
        if end-start != 1:
            flag = False
    
    graph.insert(start,end,length)

if flag:
    graph.countnum_black(graph.base[1])
    graph.sum_distance_black(graph.base[1])
    print(graph.listwise(graph.base[1]))
else:
    graph.next_black_dis(graph.base[1])
    print(graph.dfs(graph.base[1]))
    

