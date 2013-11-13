#a way to implement closures
helperArgs = 1
def printAThing(printAThingArgs):
    for x in range(printAThingArgs["aNumber"]):
        print(printAThingArgs["somethingToPrint"])

def helperFunction(closureName, argValues):
    function = information[closureName]["function"]
    argList = {eachArg:argValues[information[closureName]["args"].index(eachArg)] for eachArg in information[closureName]["args"]}
    function(argList)

helloWorld = (helperFunction("helloWorld", printAThingArgs) for y in [[]])

global information
information = {
    "helloWorld":{"function": printAThing, "args" : ["somethingToPrint", "aNumber"], "argName" : printAThingArgs},
    "helper":{"function":helperFunction, "args": ["closureName", "argValues"], "argName" : helperArgs}
}

def do(function, name,  args):
    global information[name]["argName"]
    information[name]["argName"] = args

    print(function.__name__)
    list(function)

do(helloWorld, "helloWorld", ["Stahp", 2])
