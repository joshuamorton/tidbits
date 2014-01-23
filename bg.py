import random

def isSorted(aList):
    pos = 0
    while pos < len(aList) - 1:
        if aList[pos] <= aList[pos + 1]:
            pos += 1
        else:
            return False
    return True

def bg(aList):
    x = 0
    numOfOps = 0
    while x <= len(aList):
        numOfOps += (x + 1)
        y = aList[0:x]
        random.shuffle(y)
        z = 0
        while z < len(y):
            numOfOps += (z+1)
            aList[z] = y[z]
            z += 1
        #print("sorting on the first {} numbers".format(x))
        if isSorted(aList[0:x]):
            numOfOps += (x+1)
            x += 1
        else:
            numOfOps += (x+1)
            x = 0

    return numOfOps
    return aList

def test(length, trials):
    counter = 0
    for x in range(trials):
        counter += bg(list(range(length)))
    return counter / trials