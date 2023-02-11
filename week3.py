'''Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the last occurrence of each number. For instance:

>>> remdup([3,1,3,5])
[1, 3, 5]

>>> remdup([7,3,-1,-5])
[7, 3, -1, -5]

>>> remdup([3,5,7,5,3,7,10])
[5, 3, 7, 10]'''
def binary_search(array, key):
    low=0
    high=len(array)-1
    while low<=high:
        mid=(low+high)//2
        if array[mid]==key:
            return mid
        elif array[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
def remdup(l):
    i=0
    while i<len(l):
        key=l[i]
        a=binary_search(l[i+1:],key)
        if a!=-1:           
            l.pop(a+i+1)
        else:
            i+=1
    return l

'''a=[1,2,3,4,5]
i=2
c=a[i:len(a)]
print(c)'''
print(remdup([3,1,3,5]))

# a=B_s([3,1,3,5],9)
