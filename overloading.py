#Lets have some fun.
#You know what decorators are, they look like this:

def decorator(function):
    def inner_function(*args, **kwargs):
        print args, kwargs
        x = function(*args, **kwargs)
        return x
    return inner_function

@decorator
def func(thing):
    print(thing)

func("thing")

#-----------------------------------------------------------------------------------------------

#thats pretty simple.
#now step two is a decorator that can take arguments, the code looks like this


def check(*types):
    def decorator(f):
        #shenanigans to check function arglength vs. decorator arglength
        if len(types) == f.func_code.co_argcount:
            def new_f(*args, **kwds):
                counter = 0
                for (a, t) in zip(args, types):
                    if isinstance(a, t):
                        counter += 1
                    else:
                        print "you have an error, the var \"{}\" isn't of {}".format(a, str(t))
                        raise TypeError("")
                if counter == f.func_code.co_argcount:
                    return f(*args, **kwds)
            new_f.func_name = f.func_name
            return new_f
        else:
            def fl(*args):
                print "your list of types and list of args don't match"
            return fl
    return decorator

@check(str, int)
def hai(thing, thang):
    print thing

hai("hello world", 8)
hai("hi", 8)

#-----------------------------------------------------------------------------------------------


class TypeCheck:

    def __init__(self):
        #a dict int the form {String name : Dict { Tuple (args) : Function function }}
        self.functions = {}
        pass

    def __call__(self, *types):
        def decorator(function):
            if function.func_name in self.functions:
                if types in self.functions[function.func_name]:
                    function = self.functions[function.func_name][types]
                else:
                    self.functions[function.func_name][types] = function

            #shenanigans
            if len(types) == function.func_code.co_argcount:
                print self.
                def new_function(*args, **kwargs):
                    counter = 0
                    for (a, t) in zip(args, types):
                        if isinstance(a, t):
                            counter += 1
                        else:
                            print "you have an error, the var \"{}\" isn't of {}".format(a, str(t))
                    if counter == function.func_code.co_argcount:
                        return function(*args, **kwargs)
                new_function.func_name = function.func_name
                return new_function
            else:
                def fl(*args):
                    print "you're lists don't match"
                return fl
        return decorator

checker = TypeCheck()

@checker(str)
def test(name):
    print name

test(21)