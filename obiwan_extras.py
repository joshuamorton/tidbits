"""
an incomplete library for hackish use of inline typechecked iterable
"""

import obiwan


class inline(object):
    def __init__(self, iterable):
        """
        collection is either a dict, list, set, or subtype thereof (ignoring tuples for now)
        there are probably others I forgot, and I'd be surprised if there wasn't a better way
            to do this via some kind of generic method along the lines of


            self.iterable = self.subclass(iterable)

            def subclass(self, iterable):
                class typecheckedIterable(type(iterable), typechecked):  # where typechecked is some class that does magic and provides a _check method

                    def __init__(self):
                        self.format = iterable  # provide the tyepchecking format

                    #magic to override all methods, iterables would probably need to follow some form of pseudointerface

        """
        # for now I just do it case by case, and haven't finished yet because I'm lazy and this is a proof of concept
        if isinstance(iterable, list):
            self.iterable = checked_list([], example=iterable)
        elif isinstance(iterable, dict):
            self.iterable = checked_dict({}, example=iterable)
        elif isinstance(iterable, set):
            pass

    def __rshift__(self, other):
        """
        the nice syntactic sugar
        """
        self.iterable.update(other)  # every typed iterable needs an update method, like what dict supports
        return self.iterable


def _check(example, compared):
    """
    my check function, ugly, but works, could easily replace it with duckable
    """
    if example is type(compared) or isinstance(example, (set, dict, list, tuple)) and type(example) is type(compared):
        pass
    else:
        raise obiwan.ObiwanError("The item {} is not of the type {}".format(compared, example))

    if isinstance(example, (set, dict, list, tuple)):
        if isinstance(example, dict) and len(example) == len(compared) == 1:
            #oh lord this is hacky, get keys and values into reasonable positions
            for k, v in example.items():
                pass
            for key, value in compared.items():
                pass
            _check(k, key)
            _check(v, value)
        elif isinstance(example, list):
            for item in compared:
                _check(example[0], item)
        elif isinstance(example, set):
            for v in example:
                pass
            for value in compared:
                _check(v, value)
        elif isinstance(example, tuple) and len(example) == len(compared):
            for pair in zip(example, compared):
                _check(*pair)
        else:
            raise obiwan.ObiwanError("The item {} is not of the type {}".format(compared, example))


class checked_dict(dict):
    """
    an example of an overriden iterable
    it has a template (self.example) and overrides setitem, getitem, and update
    and also needs to override a number of others to truly work properly, but this
    is hacky and I don't know the inner workings of python objects *that* well
    """
    def __init__(self, *args, example=None, **kwargs):
        self.example = example
        dict.__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        _check(self.example, {key: value})
        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        _check(list(self.example.keys())[0], key)
        return dict.__getitem__(self, key)

    def update(self, update):
        for k, v in update.items():
            self.__setitem__(k, v)


class checked_list(list):
    def __init__(self, *args, example=None, **kwargs):
        self.example = example
        list.__init__(*args, **kwargs)

    def __getitem__(self, key):
        return list.__getitem__(self, key)

    def __setitem__(self, key, value):
        _check(self.example, [value])
        list.__setitem__(self, key, value)

    def append(self, value):
        _check(self.example, [value])
        self.__iadd__([value])

    def update(self, update):
        for value in update:
            self.append(value)


x = inline({(float, type): ([int], [float], [(int, str)], {int})}) >> {(3.0, str): ([1, 2, 3], [4.0, 5.0, 6.0], [(3, "3"), (4, "4")], {1, 2, 3})}
# y = inline({(float, type): ([int], [float], [(int, str)])}) >> {(3.0, str): ([1, 2, 3], [4.0, 5.0, 6.0], [(3, "3"), (4, "4")], {1, 2, 3})} # throws an error
myList = inline([int]) >> [1, 2, 3, 4, 5]  
# how it ends up looking, and since inline is just a class, this could easily be "myList = typed([int]) >> [1,2,3,4,5,6]" or whatever

print(x)
print(myList)
# myList[2] = "help"  #throws an
