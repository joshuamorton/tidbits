import sys
import inspect
import pprint


_classes = {}
_functions = {}
_objects = {}

if __name__ != "__main__" and __name__ not in globals():
    module = sys.modules["__main__"]
    if hasattr(module, "__file__"):
        items = [line for line in inspect.getsource(module).split("\n") if __name__ in line][-1].split("from "+__name__+" import")
        print(items)

        module = __import__(module.__name__, globals(), None, [], 0)
        members = [item for item in inspect.getsource(module)]
        pprint.pprint(members)
        for name, obj in members:
            if inspect.isbuiltin(obj):
                globals()[name] = obj
            elif inspect.ismodule(obj):
                globals()[name] = obj
            elif inspect.isfunction(obj):
                globals()[name] = obj
                _functions[name] = obj
            elif inspect.isclass(obj):
                globals()[name] = obj
                _classes[name] = obj
            else:
                globals()[name] = obj
                _objects[name] = obj
    else:
        print("nope")
    print("_classes", _classes)
    print("_functions", _functions)
    print("_objects", _objects)

