'''Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the last occurrence of each number. For instance:

>>> remdup([3,1,3,5])
[1, 3, 5]

>>> remdup([7,3,-1,-5])
[7, 3, -1, -5]

>>> remdup([3,5,7,5,3,7,10])
[5, 3, 7, 10]'''
def B_s(array,key):
    low=0
    high=len(array)
    for i in range(len(array)):
        mid=int((low+high)/2)
        if key==mid:
            return(mid)
        elif(key<mid):
            high=mid-1
        else:
            low=mid+1
    return(-1)
def remdup(l):
    i=0
    for i in range(len(l)):
        dup=l[i:len(l)]
        key=l[i]
        a=B_s(dup,key)
        if a!=0:
            l.pop(a)      
    return(dup)
'''a=[1,2,3,4,5]
i=2
c=a[i:len(a)]
print(c)'''
print(remdup([3,1,3,5]))
#ERROR
'''Traceback (most recent call last):
  File "z:\Python\GitRep\NPTEL_PYTHON\week3.py", line 36, in <module>
    print(remdup([3,1,3,5]))
  File "z:\Python\GitRep\NPTEL_PYTHON\week3.py", line 27, in remdup
    key=l[i]
IndexError: list index out of range'''
# a=B_s([3,1,3,5],9)
