import math

def mergeSort(array, left, right):
    count = 0
    if left >= right-1:
        return 0

    mid_point = (left+right)//2
    count_left = mergeSort(array,left,mid_point)
    count_right = mergeSort(array, mid_point, right)
    count_merge = merge(array,left,right)
    count = count_merge + count_left + count_right
    return count

def merge(array,left, right):
    mid_point = (left + right) // 2
    a1 = array[left:mid_point]
    a2 = array[mid_point:right]

    length1=len(a1)
    length2=len(a2)

    k=left
    i=0
    j=0
    count=0


    while i<length1 and j<length2:
        if a1[i]<=a2[j]:
            array[k] = a1[i]
            i += 1
        elif a1[i]>a2[j]:
            array[k] = a2[j]
            j += 1
            count += length1 - i
        k = k+1
    while j<length2:
        array[k] = a2[j]
        j += 1
        k += 1
    while i<length1:
        array[k] = a1[i]
        i += 1
        k += 1

    return count

n = int(input())
tmp = input().split()
array = list(map(int,tmp))

count = mergeSort(array,0,n)
print(count)