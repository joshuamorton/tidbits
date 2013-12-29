import random as r
import time

def i(l):
    p = 0
    while p < len(l) - 1:
        if l[p] <= l[p + 1]:
            p += 1
        else:
            return False
    return True

def bg(l):
    x = 0
    numOfOps = 0
    while x <= len(l):
        numOfOps += (x + 1)
        y = l[0:x]
        r.shuffle(y)
        z = 0
        while z < len(y):
            numOfOps += (z+1)
            l[z] = y[z]
            z += 1
        #print("sorting on the first {} numbers".format(x))
        if i(l[0:x]):
            numOfOps += (x+1)
            x += 1
        else:
            numOfOps += (x+1)
            x = 0

    #return numOfOps
    return l

def test(length, trials):
    counter = 0
    for x in range(trials):
        counter += bg(list(range(length)))
    return counter / trials
