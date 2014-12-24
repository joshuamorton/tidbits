#naive implementation based on Haskell example code

def q(a):return a if a==[]else q([y for y in a[1:]if y<a[0]])+[a[0]]+q([y for y in a[1:]if y>=a[0]])
def q(a):return a and q([y for y in a[1:]if y<a[0]])+[a[0]]+q([y for y in a[1:]if y>=a[0]])


assert q([0,3,7,5,2,9,5,3,4,12,7,99,8,126,2,17,3,24]) == [0, 2, 2, 3, 3, 3, 4, 5, 5, 7, 7, 8, 9, 12, 17, 24, 99, 126]
assert q([]) == []

def q(*l):return[]if l==()else q(*[y for y in l[1:]if y<l[0]])+[l[0]]+q(*[y for y in l[1:]if y>=l[0]])

assert q() == []
assert q(1) == [1]
assert q(1, 12, 7, 4, 17, 6, 5, 32, 9, 12, 1, 17, 4) == [1, 1, 4, 4, 5, 6, 7, 9, 12, 12, 17, 17, 32]

#def q(x,*s):return x and q(*[y for y in s if y<x]) +[x]+q(*[y for y in s if y>=x])

assert q() ==[]