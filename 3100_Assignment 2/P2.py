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

def answer_for_one_query(array,n):
    s = Stack()
    max_product = 0
    
    for i in range(n):
        if s.size == 0 or array[s.peek()]<=array[i]:
            s.push(i)
        else:
            while (s.size>0 and array[s.peek()]>array[i]):
                mini_height_index = s.pop()
                mini_height = array[mini_height_index]
                if s.size == 0:
                    width = i
                else:
                    width = i-s.peek()-1
                product_area = width*mini_height
                if product_area>max_product:
                    max_product=product_area
            s.push(i)
    while s.size>0:
        height = array[s.pop()]
        if s.size==0:
            width = n
        else:
            width = n-s.peek()-1
        product_area = width*height
        if product_area>max_product:
                    max_product=product_area
    return max_product



if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        l = list(map(int,input().split()))
        print(answer_for_one_query(l,n))