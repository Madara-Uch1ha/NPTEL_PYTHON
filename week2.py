# print(primepartition(185))
# print(isprime(185))
"""A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and
q are prime numbers.
Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned
as primes and False otherwise. (If m is not positive, your function should return False.)
Here are some examples of how your function should work."""


def isprime(m):
    flag = 0
    for i in range(1, int((m / 2)) + 1):
        if m % i == 0:
            flag += 1
    if flag == 1:
        return 1
    else:
        return 0


def primepartition(m):
    flag = 0
    for i in range(1, int(m ** 0.5) + 1):
        if isprime(i):
            c = m - i
            if isprime(c):
                flag = 1
                break
    if flag == 0:
        return False
    else:
        return True


# Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched:
# that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should
# ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if
# it does not.
# Here are some examples to show how your function should work.
# a=list(["q",8,"k","j","n","k","l"])
# print(a)
def matched(s):
    stk = str(list(s))
    flag = 0
    i = 0
    for i in range(len(stk)):
        if flag == -1:
            return False
        if stk[i] == "(":
            flag += 1
            i += 1
        elif stk[i] == ")":
            flag -= 1
            i += 1
    if flag == 0:
        return True
    else:
        return False


# print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))

"""A list rotation consists of taking the first element and moving it to the end. For instance, if we rotate the list 
[1,2,3,4,5], we get [2,3,4,5,1]. If we rotate it again, we get [3,4,5,1,2]. 
Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns the list l after k 
rotations. If k is not positive, your function should return l unchanged. Note that your function should not change l 
itself, and should return the rotated list. 
Here are some examples to show how your function should work."""
def rotatelist(l,k):
    if k<=0:
        return 1
    k=k%len(l)
    return(l[k:]+l[:k])
# print(rotatelist([1,2,3,4,5,6],3))