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

    new_obj["_init"](*args)
    return new_obj


x = new_object(obj)
print x["_str"]()

# now to deal with inheritence and an inheritant object model
# we need a way to define a class in code, because building each class like we
# did for obj would be a pain

def new_class(parent, *instance_data, **methods):
    new_cls = {val:parent[val] for val in parent}  # inheritence
    new_cls["_parent_class"] = parent  # keep track of parent for reasons?
    for value in instance_data:
        new_cls[value] = None  # this isn't strictly necessary
    for method in methods:
        new_cls[method] = methods[method]  # this is though
    return new_cls


def init_person(instance, name, age):
    instance["name"] = name
    instance["age"] = age

def person_string(instance):
    return "<Hi my name is "+instance["name"]+">"

def is_older(instance, other):
    return instance["age"] > other["age"]


Person = new_class(obj, "name", "age", _init=init_person, _str=person_string, is_older=is_older)

john = new_object(Person, "john", 35)
amy = new_object(Person, "amy", 26)

print john["age"]
print john["name"]
print john["_str"]()
print amy["is_older"](john)

Child = new_class(Person, is_teen=lambda inst: 20 > inst["age"] > 12)

billy = new_object(Child, "billy", 7)
print billy["is_teen"]()
print billy["age"]