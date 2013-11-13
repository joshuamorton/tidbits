def mergeSort(aList):
    splitPosition = len(aList) / 2
    if splitPosition < 1:
        return aList
    else:
        listOne = aList[:int(round(splitPosition))]
        listOne = mergeSort(listOne)
        listTwo = aList[int(round(splitPosition)):]
        listTwo = mergeSort(listTwo)
        
        listOneIndex = 0
        listTwoIndex = 0
        newList = []

        while listOneIndex + listTwoIndex < splitPosition * 2:
            if listOneIndex < len(listOne) and listTwoIndex < len(listTwo):
                if listOne[listOneIndex] <= listTwo[listTwoIndex]:
                    newList.append(listOne[listOneIndex])
                    listOneIndex += 1
                else:
                    newList.append(listTwo[listTwoIndex])
                    listTwoIndex += 1
            else:
                if listOneIndex <= listTwoIndex:
                    newList.append(listOne[listOneIndex])
                    listOneIndex += 1
                else:
                    newList.append(listTwo[listTwoIndex])
                    listTwoIndex += 1
        return newList


#mergeSort(list(range(90000,1,-1)))

def binaryCount(aNum):
    log = 0
    num = aNum
    while num > 1:
        log += 1
        num = num / 2
    numList = []
    num = aNum
    position = log
    while len(numList) <= log:
        if num - 2 ** position >= 0:
            numList.append(True)
            num = num - 2 ** position
        else:
            numList.append(False)
            num = num
        position -= position
    print(numList)

def binaryConvert(aList):
    position = len(aList)
    while position >= 0:
        

#list(range(100000,1,-1)).sort()
