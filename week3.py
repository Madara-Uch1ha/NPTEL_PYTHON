'''def remdup(l):
    temp=[]
    l.reverse()
    for  i  in range(len(l)):
        if l[i] not in temp:
            temp.append(l[i])
    temp.reverse()
    return temp

def splitsum(l):
     pos=0
     neg=0
     for n in l:
         if n>0:
             pos=pos+n**2  
         else :
             neg=neg+n**3
     return([pos,neg])

def matrixflip(m, d):
    if d == 'h':
        return [row[::-1] for row in m]
    elif d == 'v':
        return m[::-1]
    else:
        return m'''

def remdup(l):
    lis2=list()
    l.reverse()
    for  i  in range(len(l)):
        if l[i] not in lis2:
            lis2.append(l[i])
    lis2.reverse()
    return lis2
'''Write a Python function splitsum(l) that takes a nonempty list of integers and returns a list [pos,neg], where pos is the sum of squares all the positive numbers in l and neg is the sum of cubes of all the negative numbers in l.

Here are some examples to show how your function should work.

>>> splitsum([1,3,-5])
[10, -125]

>>> splitsum([2,4,6])
[56, 0]

>>> splitsum([-19,-7,-6,0])
[0, -7418]

>>> splitsum([-1,2,3,-7])
[13, -344]'''

def splitsum(l):
     (pos,neg)=(0,0)
     for n in l:
         if n>0:
             pos=pos+n**2  
         else :
             neg=neg+n**3
     return([pos,neg])

'''A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3
4  5  6 
7  8  9
would be represented as [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

A horizonatal flip reflects each row. For instance, if we flip the previous matrix horizontally, we get

3  2  1
6  5  4 
9  8  7
which would be represented as [[3, 2, 1], [6, 5, 4], [9, 8, 7]].

A vertical flip reflects each column. For instance, if we flip the previous matrix that has already been flipped horizontally, we get

9  8  7
6  5  4 
3  2  1
which would be represented as [[9, 8, 7], [6, 5, 4], [3, 2, 1]].

Write a Python function matrixflip(m,d) that takes as input a two dimensional matrix m and a direction d, where d is either 'h' or 'v'. If d == 'h', the function should return the matrix flipped horizontally. If d == 'v', the function should retun the matrix flipped vertically. For any other value of d, the function should return m unchanged. In all cases, the argument m should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> myl = [[1,2],[3,4]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(myl,'h')
[[2, 1], [4, 3]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(myl,'v')
[[3, 4], [1, 2]]  

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(matrixflip(myl,'h'),'v')
[[4, 3], [2, 1]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(matrixflip(myl,'h'),'v')
[[4, 3], [2, 1]]

>>> myl
[[1, 2], [3, 4]]'''
def matrixflip(m, d):
    if d == 'h':
        return [row[::-1] for row in m]
    elif d == 'v':
        return m[::-1]
    else:
        return m