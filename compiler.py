#a fully functional compiler for brainfuck written in vanilla python

# to do: add interpreted mode

#brainfuck syntax:
# > increment data pointer
# < decrement data pointer
# + increment the byte at said pointer
# - decrement the byte at said pointer
# . output the byte at the pointer
# , accept a byte of input and store its value in the data pointer
# [ if the byte is zero, jump forward to the correclty matched ] else continue
# ] if the byte is nonzero jump back tot he correctly matched [ and continue

def interpreter():
    """"""
    print("""Welcome to Brainfuck, this compiler will eventually do some cool things, 
but for now this is just a shell that does not save anything between runs.  
Type help for syntax information, quit to exit and return to python, or 
code to run it.  This is a work in progress. Type "help" for help, "examples" 
for examples, or "quit" to return to vanilla python.
\nJosh Morton """)
    myActive = True
    while myActive == True:
        myinput = input("!?:::")
        if myinput == "quit" or myinput == "q" or myinput == "Quit" or myinput == "QUIT" or myinput == "exit" or myinput == "Exit" or myinput == "EXIT":
            myActive = False
        elif myinput == "help" or myinput == "h" or myinput == "Help" or myinput == "HELP":
            print(
    """ This is the interpreted mode for this command line brainfuck compiler.  
    In case you are unaware, these are the brainfuck commands:
    > increment the data pointer
    < decrement the data pointer
    + increment the byte at the current position
    - decrement the byte at the current position
    . output the contents of the current position
    , take a user input and store it to the current byte
    [ begin a loop
    ] end a loop
                """)
        elif ">" in myinput or "<" in myinput or "[" in myinput or "," in myinput or "." in myinput or "+" in myinput or "-" in myinput:
            compiler(myinput)
        elif myinput == "examples":
            print("""Pick a piece of example code, here are some options.  Type the name in terminal to see it:
    "Hello World"
    "Fibonacci"
    "Adder"
                """)
        elif myinput == "Hello World":
            print("""++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.""")
            compiler("""++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.""")
        elif myinput == "Fibonacci":
            print("+.>+.>>>+++++ +++++[<<<[->>+<<]>>[-<+<+>>]<<<[->+<]>>[-<<+>>]<.>>>-]")
            compiler("+.>+.>>>+++++ +++++[<<<[->>+<<]>>[-<+<+>>]<<<[->+<]>>[-<<+>>]<.>>>-]")
        elif myinput == "Adder":
            print(",>,<[>+<-]>.")
            compiler(",>,<[>+<-]>.")

charList = [">", "<", "+", "-", ".", ",", "[","]"]

def stringCleaner(inputString):
    """"""
    returnList = []
    for eachChar in inputString:
        if eachChar in charList:
            returnList.append(eachChar)
    return returnList

def greaterThan(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    if memoryPosition >= len(memory):
        memory.append(0)
        if memoryPosition == len(memory):
            memoryPosition += 1
        else:
            memory.append(0)
            memoryPosition += 1
    else:
        if memoryPosition == len(memory):
            memoryPosition += 1
        else:
            memoryPosition += 1
    position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def lessThan(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""
    if memoryPosition == 0:
        print("\n You have referenced a nonexistent part of memory at character number {0}  (a '<') in your code".format(position+1))
        contentList = [""]
        position = 100
    else:
        memoryPosition -= 1
    position += 1
    return(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)

def plusSign(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""
    #if memory[memoryPosition] == None:
    #    memory[memoryPosition] = 0
    if memoryPosition >= len(memory):
        memory.append(0)
    memory[memoryPosition] += 1
    position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)

def minusSign(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""
    if memoryPosition >= len(memory):
        memory.append(0)
    if memory[memoryPosition] == 0:
        print("\n You are attempting to subtract from 0 at character number {0} in your code".format(position+1))
        contentList = [""]
        position = 100
    else:
        memory[memoryPosition] -= 1
    position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)

def period(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""
    if memoryPosition >= len(memory):
        print("You are trying to print at a nonexistent position in memory at character {} in your code".format(position+1))
        memory.append(0)
    else:
        print(chr(memory[memoryPosition]), end = "")
        #print(memory[memoryPosition])
    position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)

def comma(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""
    if memoryPosition >= len(memory):
        memory.append(0)
    memory[memoryPosition] = int(input("Input an integer value: "))
    position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)

def leftBracket(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""    
    if memoryPosition >= len(memory):
        memory.append(0)
    elif memory[memoryPosition] == 0:
        momentaryCount = 1
        counter = 1
        while  momentaryCount > 0:
            if contentList[position+counter] == "[":
                momentaryCount += 1
                counter += 1
            elif contentList[position+counter] == "]":
                momentaryCount -= 1
                counter += 1
            else:
                counter += 1
        position += counter
    else:
        loopCount += 1
        loopPosition[loopCount] = position
        position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)

def rightBracket(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""
    if loopCount == 0:
        position += 1 
        loopCount -= 1
    else:
        position = loopPosition[loopCount]
        loopCount -= 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def runCode(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """"""
    if len(memory) > 100:
        return
    if character == ">":
        retVal = greaterThan(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    elif character == "<":
        retVal = lessThan(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    elif character == "+":
        retVal = plusSign(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    elif character == "-":
        retVal = minusSign(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    elif character == ".":
        retVal = period(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    elif character == ",":
        retVal = comma(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    elif character == "[":
        retVal = leftBracket(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    elif character == "]":
        retVal = rightBracket(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        return retVal
    else:
        position += 1
        return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def compiler(inputString):
    """"""
    contentList = stringCleaner(inputString)
    position = 0
    memoryPosition = 0
    memory = []
    loopCount = 0
    loopPosition = {}
    while position < len(contentList):
        retVals = runCode(contentList, contentList[position], position, memory, memoryPosition, loopCount, loopPosition)
        #print(retVals[2])
        contentList = retVals[0]
        position = retVals[2]
        memory = retVals[3]
        memoryPosition = retVals[4]
        loopCount = retVals[5]
        loopPosition = retVals[6]
        #print(loopPosition)
        #print(memory, " memPosition ",str(memoryPosition), " codePosition ", str(position), "loop", loopCount, " loopList ", loopPosition)
    print("\n", end = "")
