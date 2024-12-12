def mergeSort(array, left, right,pos=0):
    if right-left<=1:
        return [array[left]]
    mid_point = (left+right)//2
    left_array = mergeSort(array,left,mid_point)
    right_array = mergeSort(array, mid_point, right)
    merged = merge(left_array,right_array,pos)
    return merged

def merge(left_array, right_array,pos=0):
    m = []

    length1=len(left_array)
    length2=len(right_array)
    i=0
    j=0
    while i<length1 and j<length2:
        if left_array[i][pos]<=right_array[j][pos]:
            m.append(left_array[i])
            i += 1
        elif left_array[i][pos]>right_array[j][pos]:
            m.append(right_array[j])
            j += 1
    while j<length2:
        m.append(right_array[j])
        j += 1
    while i<length1:
        m.append(left_array[i])
        i += 1
    return m

class Stack:
    def __init__(self):
        self.data = list()
        self.size = 0
    
    
    def push(self,e):
        self.size += 1
        return self.data.append(e)
    
    
    def pop(self):
        if self.size ==0:
            return 
        else:
            self.size -=1
            return self.data.pop()
        
        
    def peek(self):
        if self.size ==0:
            return 
        else:
            return self.data[self.size-1]
        
        
if __name__ == "__main__":
    s = Stack()
    data_list = []

    n=int(input())
    for i in range(n):
        num = i
        floor , hp , d = input().split()
        player = (int(floor), int(hp), d, num)
        data_list.append(player)
    new_list = sorted(data_list,key=lambda s: s[0])
    for player in new_list:
        if s.size==0 or s.peek()[2]=="D" or player[2] == "U":
            s.push(player)

        elif s.peek()[2]=="U" and player[2] == "D":
            while (not s.peek() is None) and s.peek()[2] == "U":
                defender = s.pop()
                defender_hp = defender[1]
                player_hp = player[1]
                if player_hp==defender_hp:
                    player = (player[0],0 , player[2], player[3])
                    break
                elif player_hp>defender_hp:
                    player = (player[0],player_hp-1 , player[2], player[3])
                    continue    
                elif player_hp<defender_hp:
                    player = (player[0],0 ,player[2], player[3])
                    defender = (defender[0],defender_hp-1 , defender[2], defender[3]) 

                    s.push(defender)

                    break
            if player[1]>0:
                s.push(player)
    survivors = s.data
    final =  sorted(survivors,key=lambda s: s[3])
    for player in final:
        print(player[1])
        

    
