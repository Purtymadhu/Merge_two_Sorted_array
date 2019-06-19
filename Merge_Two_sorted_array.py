from heapq import merge
p,q=map(int,input("Enter the size of the array").split())
a=list(map(int,input("enter array elements of A array").split()))
b=list(map(int,input("enter array elements of B array").split()))
c=list(merge(a,b))
print(*c)
