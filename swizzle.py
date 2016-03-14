class CommaFreeError(Exception):
    pass


class SwizzleMeta(type):
    def __new__(self, name, bases, attrs):
        old = attrs['__init__']
        slots = set(attrs['__slots__'])

        def init_wrapper(self, *args, **kwargs):
            old(self, *args, **kwargs)
            for x in slots:
                for z in slots - {x}:
                    for y in slots - {x, z}:
                        if y in x+z:
                            raise CommaFreeError(y+" is in "+x+z)

        attrs['__init__'] = init_wrapper
        
        return super().__new__(self, name, bases, attrs)


class Swizzler(object, metaclass=SwizzleMeta):
    __slots__ = []

    def __getattr__(self, attr):
        attrs = (a for a in set(type(self).__slots__) if a in attr)
        attrs = sorted(attrs, key=lambda a: attr.index(a))
        return tuple(self.__getattribute__(a) for a in attrs)

    def __setattr__(self, key, value):
        attrs = [a for a in set(type(self).__slots__) if a in key]
        if len(attrs) in (1, 0):
            super().__setattr__(key, value)
        else:
            pairs = zip(sorted(attrs, key=lambda a: key.index(a)), value)
            for k, v in pairs:
                super().__setattr__(k, v)

    def __init__(self):
        pass


if __name__ == "__main__":
    class Vec4(Swizzler):
        __slots__ = ["x", "y", "z", "w"]
        def __init__(self, x, y, z, w):
            self.x = x
            self.y = y
            self.z = z
            self.w = w

    a = Vec4(1,2,3,4)
    b = Vec4(5,6,7,8)
    print(b.xyzw)
    print("should be 5, 6, 7, 8")
    b.xyz = a.yzw
    print(b.xyzw)
    print("should be 2, 3, 4, 8")

    class ComplexSwizz(Swizzler):
        __slots__ = ["hello", "world"]
        def __init__(self, hello, world):
            self.hello = hello
            self.world = world


    c = ComplexSwizz("hi", "mundo")
    d = ComplexSwizz("Aloha", "word")
    c.worldhello = d.helloworld
    print(c.helloworld)
    print("should be word, Aloha")

    class ErrSwizz(Swizzler):
        __slots__ = ["cat", "attack", "loc"]
        def __init__(self, cat, attack, loc):
            self.cat = cat
            self.attack = attack
            self.loc = loc

    e = ErrSwizz("bang", "boom", "pow")
