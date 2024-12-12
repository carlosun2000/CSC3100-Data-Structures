memory_dict = dict()

def matrix_multiplication(matrix1,matrix2):
    a1,a2,a3,a4 = matrix1
    b1,b2,b3,b4 = matrix2
    return ((a1*b1+a2*b3)%m,(a1*b2+a2*b4)%m,(a3*b1+a4*b3)%m,(a3*b2+a4*b4)%m)

def matrix_power(a,b,n):
    if n in memory_dict.keys():
        return memory_dict[n]

    if n == 1:
        return (a%m,b%m,1,0)

    n1 = n//2
    n2 = n - n1
    result = matrix_multiplication(matrix_power(a,b,n1),matrix_power(a,b,n2))

    memory_dict[n]= result
    return result

def get_fn(matrix):
    a1,a2,a3,a4 = matrix
    fn = ((a1*f1)%m+(a2*f0)%m)%m
    return fn

n,a,b,f0,f1,m = list(map(int,input().split()))
if n==1:
    print(f1)
else:
    matrix = matrix_power(a,b,n-1)
    print(get_fn(matrix))