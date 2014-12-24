
#Joshua morton
#joshua.morton@gmail.com
#I completed this assingment alone, although I used some stuff to get brainfuck syntax info, I believe http://esolangs.org/wiki/Brainfuck was used to some degree.

#To help you out, a heavily commented version


#------------------------------------------------------------------------------
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

global savedState # probably unnecessary global for a most likley not needed variable
savedState = {} #a variable to save the state at the beginning of loops for infinite loop protection
global caseCounter
caseCounter = 0 #variable to keep track of loop numbers to stop infinite looping

def interpreter():
    """The interpreter function controls the user interface that the user engages with.  
    It provides output and help information, takes in user input, and outputs the 
    results of code."""

    #todo: add a numerical i/o mode vs. the current ascii output only mode

    print("""Welcome to Brainfuck, this compiler will eventually do some cool things, 
but for now this is just a shell that does not save anything between runs.  
Type help for syntax information, quit to exit and return to python, or 
code to run it.  This is a work in progress. Type "help" for help, "examples" 
for examples, or "quit" to return to vanilla python.
\nJosh Morton """)
    myActive = True #keeps you in the user input mode
    while myActive == True: #works with above
        myinput = input("!?:::") #sets the UI input to look pretty and not confuse with code syntax
        if myinput == "quit" or myinput == "q" or myinput == "Quit" or myinput == "QUIT" or myinput == "exit" or myinput == "Exit" or myinput == "EXIT": #options for user input, to make it 
            myActive = False #exits the UI
        elif myinput == "help" or myinput == "h" or myinput == "Help" or myinput == "HELP": #options for user input
            print( #A giant list of elifs to check and see what the user wants
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
    Memory is not conserved between actions, 
    type "help X" for more information regarding a specific character (function)""")
        elif myinput == "help >":
            print("""Moves the data pointer to the right, if you are currently at the end of the memory tape, it will create a new block
                at the end of the tape and set its value to 0""")
        elif myinput == "help <":
            print("""Moves the data pointer to the left.  Will throw an error if the current pointer is at position zero in memory.""")
        elif myinput == "help +":
            print("""Increments the current data pointer""")
        elif myinput == "help -":
            print("decrements the current data pointer.  Will throw an error if the current pointer is equal to zero")
        elif myinput == "help .":
            print("""Output the ascii value of the current block, it is printed without any newline, so if memory at the current block is
                equal to 65, ".." will print "AA". """)
        elif myinput == "help ,":
            print("""Takes user input as an integer value and saves it to the current memeory position.  This will only take ascii value inputs,
                so for example typing "A" when input is prompted will throw an error.""")
        elif myinput == "help [":
            print("""Begins a loop, the interpreter will support multiple nested loops and will ignore extranious ] characters, however it will also
                evaluate ] on a first come, first serve basis.  This means that while in general, arbitrary text can be placed [>][here] within code,
                '[>]["]"' is a character"] will be evaluated the same as '[>]["]'. """)
        elif myinput == "help ]":
            print("""ends a loop.  See 'help [' for more detailed information.""")
        elif ">" in myinput or "[" in myinput or "," in myinput or "+" in myinput: #one of those 6 chars must be in the code for it to ever work.
            compiler(myinput) #THIS ONE ACTUALLY RUNS THE REST OF THE CODE
        elif myinput == "examples":
            print("""Pick a piece of example code, here are some options.  Type the name in terminal to see it:
    "Hello World"
    "Fibonacci"
    "Adder"
                """)
        elif myinput == "Hello World": #some pieces of example code to be run by the user.
            print("""++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.""")
            compiler("""++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.""")
        elif myinput == "Fibonacci":
            print("+.>+.>>>+++++ +++++[<<<[->>+<<]>>[-<+<+>>]<<<[->+<]>>[-<<+>>]<.>>>-]")
            compiler("+.>+.>>>+++++ +++++[<<<[->>+<<]>>[-<+<+>>]<<<[->+<]>>[-<<+>>]<.>>>-]")
        elif myinput == "Adder":
            print(",>,<[>+<-]>.")
            compiler(",>,<[>+<-]>.")


charList = [">", "<", "+", "-", ".", ",", "[","]"] #list for checking where things are


def stringCleaner(inputString):
    """Removes nonessential characters, for example plaintext, from the code.  
    This makes commenting in your code really, really easy"""

    #todo: nothing

    returnList = [] #creates a list from the text
    for eachChar in inputString:
        if eachChar in charList: #removes random crap from the string
            returnList.append(eachChar)
    return returnList #now you have a list of characters, instead of a string, not that this matters much.


def greaterThan(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """This is the code to increment the memory pointer by 1 position.  There is a safeguard built in
    that will add a new block to memory if you are at the end of the current memory list"""

    #todo: nothing

    if memoryPosition >= len(memory): #a check to add a new memory block if you are at the "right" side of the list
        memory.append(0) #adds the new item to the memory list
        if memoryPosition == len(memory): #check if you are at the end
            memoryPosition += 1 #move right
        else: #all of the others are basically the same
            memory.append(0)
            memoryPosition += 1
    else:
        if memoryPosition == len(memory):
            memoryPosition += 1
        else:
            memoryPosition += 1
    position += 1 #next character in the code
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def lessThan(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """Will move the pointer back one position, this code contains my first homemmade error message"""

    #todo: nothing

    if memoryPosition == 0: #check to see if you're trying to move left from position 0
        print("\n You have referenced a nonexistent part of memory at character number {0}  (a '<') in your code".format(position+1)) #error code!
        contentList = [""]
        position = 100 #These two lines together will stop code execution by placing you well beyond the end of the code, sloppy but functional
    else:
        memoryPosition -= 1 #move left
    position += 1 #go to the next character in the code
    return(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def plusSign(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """increments the value at the current position"""

    #todo: nothing

    if memoryPosition >= len(memory): #check to see if you're at the far right/beyond the far right, though normally this is only relevant if this is the very first character
        memory.append(0)
    memory[memoryPosition] += 1 #increment value
    position += 1 #move forward in code
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def minusSign(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """Decrements the value at the current position, again there is a homemmade error message"""

    #todo: nothing

    if memoryPosition >= len(memory): #check for position in code, and keep you from trying to append to nonexistand memory this should never actually be relevantsince "-" can't begin code, but meh.
        memory.append(0)
    if memory[memoryPosition] == 0:
        print("\n You are attempting to subtract from 0 at character number {0} in your code".format(position+1)) #error code
        contentList = [""]
        position = 100 #breaks out of loop/code
    else:
        memory[memoryPosition] -= 1 #decrements value at location
    position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def period(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """will print the value at the current position in memory, ascii encoded because that's how BF works, the 
    commented out portion is for code that, for example, prints Fibonacci numbers.  If the numbers are ascii
    encoded, you end up with weird results"""

    #todo: add the two version mode
    #todo: add self-rolled ascii encoding, with a dictionary and lookup function, because currently some low ascii values (like null) don't print anything to the command line, which is awkward

    if memoryPosition >= len(memory): #check to see if you're at the end
        memory.append(0)
    print(chr(memory[memoryPosition]), end="") #converts character to ascii and prints it, end="" doesn't function in python2, hence multiple versions
    #print(memory[memoryPosition])
    position += 1
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def comma(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """Takes in user input, currently only as an integer, and saves it to the current memory block, overwriting
    whatever was previously there"""

    #todo: add ascii input mode?

    if memoryPosition >= len(memory): #position check
        memory.append(0)
    try:
        memory[memoryPosition] = int(input("Input an integer value: ")) #takes input as an integer, raw_input in python 2 and calico python versions.
        position += 1
        return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
    except ValueError: #protection from people entering things like "YOLO420HAHAHANOWAYBRUHHH!"
        print("Your input was not a number, try again")
        return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)



def leftBracket(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """Begins loops, the loopCount and loopPosition variables keep track of the most recent loop in case
    there are nested loops.  LoopCount is simply a number that increments with every relevant left bracket and decrements with every right bracket"""

    global caseCounter #keeps it global up in here

    #todo: add infinite loop protection # and now nothing
    #most  test cases work, ">+[>X]" still causes issues.
    #Finally fixed!

    if position >= len(contentList)-1: #the bracket is the last character, derp.
        print("You have an unmatched bracket in your code, it will not run.") #throw error
        position = 100
        contentList = [""]
        return(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
    if memoryPosition >= len(memory): #same protection, also shouldn't be relevant
        memory.append(0)
    elif memory[memoryPosition] == 0: #if the position is 0, you just skip forward and reset everything to 0
        caseCounter = 0 #resets caseCounter because the loop has been broken
        momentaryCount = 1 #keeps track of number of left brackets ther have been
        counter = 1 #number of spaces forward that you've moved
        while  momentaryCount > 0:
            if position+counter >= len(contentList): #something is wrong
                print("You have an unmatched left bracket in your code, it will not run.") #throw error
                position = 100
                contentList = [""] 
                return(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
            elif contentList[position+counter] == "[": #sees left bracket, momentary count +1
                momentaryCount += 1
                counter += 1
            elif contentList[position+counter] == "]": #sees right bracket, momentary count -1
                momentaryCount -= 1
                counter += 1
            else:
                counter += 1 #any other character, moves forward
        position += counter #jumps to end of loop
    else:
        caseCounter += 1 #an infinite loop will always come through here and only here, it will not be reset by any of the caseCounter = 0 resets.
        if caseCounter > 100:
            print("you seem to have an infinite loop in your code.  you should look over that and fix it.") #throw error
            position = 100
            contentList = [""]
            return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        loopCount += 1
        loopPosition[loopCount] = position
        position += 1
        #savedState keeps tack of the situation when a loop is started, but I have max loop protection, so this isn't strictly necessary.
        global savedState
        savedState[loopCount] = (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)

def rightBracket(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """Ends a loop, currently extranious right brackets are ignored"""

    #todo: nothing

    if loopCount == 0: #checks if you are in a loop
        position += 1 
        print("You seem to have an unmatched right bracket, I've ignored it, but you might have an error.  Its at character {} in your code".format(position)) #yells at you for that problem
    else:
        #print(contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        global savedState #this is probably unnecessary
        #print(savedState) #debugging
        #print(loopCount) #debugging
        #dear god this line is disgusting.  I'm so sorry, and what's more, I don't think much of it is necessary.
        if (savedState[loopCount][4] == memoryPosition and savedState[loopCount][3][savedState[loopCount][4]] < memory[memoryPosition]):# or (len(savedState[loopCount][3]) < len(memory) and memory[memoryPosition] >= 0 and memoryPosition >= savedState[loopCount][4]):
            print("You seem to have in infinitely recurring loop in your code.  You should fix that.")
            position = 100
            contentList = [""] #break out of loop
            return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)
        position = loopPosition[loopCount] #sets the position to loopcount, a dict of loops and numbers that correspond to them
        loopCount -= 1 #ends the current loop
    return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition)


def runCode(contentList, character, position, memory, memoryPosition, loopCount, loopPosition):
    """Checks the character, and runs the appropriate code"""

    #todo: nothing

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
        return (contentList, character, position, memory, memoryPosition, loopCount, loopPosition) #skips anything random that somehow made it through the previous code protection


def compiler(inputString):
    """Keeps track of all variables and moves everything around, runs it all in a while loop to loop through the entire program"""

    #todo: nothing

    contentList = stringCleaner(inputString) #cleans the code
    position = 0 #initializes variables
    memoryPosition = 0
    memory = []
    loopCount = 0
    loopPosition = {}
    while position < len(contentList):
        retVals = runCode(contentList, contentList[position], position, memory, memoryPosition, loopCount, loopPosition) #runss the character
        #print(retVals[2]) #debugging
        contentList = retVals[0] #updates values
        position = retVals[2]
        memory = retVals[3]
        memoryPosition = retVals[4]
        loopCount = retVals[5]
        loopPosition = retVals[6]
    global caseCounter
    caseCounter = 0 #resets the loop count infinite loop protection
        #print(loopPosition) #debugging
    print("\n", end = "") #unsure of best way to print things

def automatedTest(length = 5): #this doesn't actually change anything, making it work would be difficult.
    """An automated testing suite, will run the compiler through its paces, testing every string of length 5.  Be careful,
    this will run through nearly 17000 (7^5) test cases.  It will take some time."""

    charList = [">","<","+","-",".","[","]"]
    reallyBigList = [a+b+c+d+e for a in charList for b in charList for c in charList for d in charList for e in charList] #ohgod, a list of length 17000+
    for eachExample in reallyBigList:
        print(reallyBigList.index(eachExample))
        print(eachExample)
        compiler(eachExample) #runs the code on every item in the list, and prints some info.
        print("Next Case \n")

interpreter()