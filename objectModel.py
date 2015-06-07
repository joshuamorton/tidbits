from types import FunctionType
# lets build an object model that supports single inheritence in python
# we can restrict ourself to only defining functions and using dictionaries
# nothing else is necessary, and the only additions we could make are syntactic
# sugar (for example defining __getattr__ on our "objects" so that we can use
# dotted access)

# we start with something simple, a base object that everything else inherits
# from, it is simply a dictionary

obj = dict()

# now we decide on an api for our object model, in this case we'll say that 
# "_init" is our initializer, and "_str" is our toString/__str__ method,
# everything else will come later, as that's all we need for now
# We also need to store the name of our class on in it, under "_name"

def string_function(instance):
    return "<instance of "+instance["_name"]+">"

# here I sneak into python level code to allow us to differentiate between
# things

obj["_str"] = string_function

# our default initialize doesn't need to do anything
def initialize(instance):
    pass

obj["_init"] = initialize
obj["_name"] = "obj"

# the last thing is that a class needs to keep track of its parent such that you
# can actually make use of inheritence, note that this is not object level but
# class level
obj["_parent_class"] = obj

# now we need to define a class level new method that will generate new
# instances of the class, this is likely going to be very generalizeable

# but first, a bit of magic:

def bind_method(instance, method):
    def bound_method(*args, **kwargs):
        return method(instance, *args, **kwargs)
    return bound_method

# that oddly resembles a simplified version of functools.partial
# and the magic part is that now you don't need to pass the instance in when
# calling from the class

def new_object(clazz, *args):
    new_obj = {}
    # iterate through all 
    for value in clazz:
        if isinstance(clazz[value], FunctionType):
            new_obj[value] = bind_method(new_obj, clazz[value])
        else:
            new_obj[value] = clazz[value]

    new_obj["_init"]()
    return new_obj


x = new_object(obj)
print x["_str"]()