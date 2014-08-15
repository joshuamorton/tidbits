import json
import sys
import re

# aww yiss...
def parse(s): return json.loads('['+re.sub('([")])\s*(["(])','\g<1>,\g<2>',re.sub('[^()\s]+','"\g<0>"',s)).replace('(','[').replace(')',']')+']')

class Scope(object):
    def __init__(self, parent, names=[], values=[]):
        self.parent = parent
        self.values = { name: value for name, value in zip(names, values) }
    def __getitem__(self, name):
        return self.values[name] if name in self.values else self.parent[name]

def _define(n,e): 
        g[_eval(n)] = _eval(e)

def _lambda(argnames, body):
    _scope = scopes[-1]
    def newfunc(*args):
        fscope = Scope(_scope, argnames, [_eval(a) for a in args])
        scopes.append(fscope)
        ret = _eval(body)
        scopes.pop()
        return ret
    return newfunc

g = {
    '+': lambda *args: sum(_eval(a) for a in args),
    '-': lambda a,b: _eval(a) - _eval(b),
    '/': lambda a,b: _eval(a) / _eval(b), #added division
    '*': lambda *args: reduce(lambda a,b: a*b, (_eval(a) for a in args)),
    '=': lambda a,b: _eval(a) == _eval(b),
    'define': _define,
    'str': lambda *args: ' '.join(args),
    'list': lambda *args: tuple(_eval(a) for a in args),
    'lambda': _lambda,
    'do': lambda *args: eval(args[0])(*[_eval(i) for i in args[1:]]),
    'exit': lambda *args: sys.exit(),
    'if': lambda e, y, n: _eval(y) if _eval(e) else _eval(n),
    'int': lambda x: int(_eval(x))
}
scopes = [ g ]

def _eval(expr):
    if isinstance(expr, list):
        return _eval(expr[0])(*expr[1:])
        #there needs to be a way to deal with booleans from inside the lisp itsself
    elif expr == "True":
        return True
    elif expr == "False":
        return False
    elif isinstance(expr, basestring):
        try:
            return scopes[-1][expr] if ord(expr[0]) not in range(ord('0'), (ord('9') + 1)) else float(expr)
        except:
            return expr
    else:
        return expr

def shell():
    sys.stdout.write('>> ')
    sys.stdout.flush()
    level = 0
    _buffer = ''
    while True:
        line = sys.stdin.readline()
        for char in line:
            if char == '(': level += 1
            elif char == ')': level -= 1
            _buffer += char
        if level == 0:
            for stmt in parse(_buffer):
                print(_eval(stmt))
            return

if __name__ == '__main__':
    while True:
        try:
            shell()
        except Exception as e:
            print('Error:', e)


"""useful functions:
factorial : (define fact (lambda (x) (if (= x 1) 1 (* x (fact (- x 1))))))
power : (define pow (lambda (number power) (if (= power 1) number ( * number (pow number (- power 1))))))
not equals : (define != (lambda (a b) (if (= a b) False True)))
import arbitrary builtin modules: (define import (lambda (module) (define module (do __import__ module)))) //then you can do (import math) and math will be
(define attr (lambda (module attr) (define attr (do getattr module attr))))
"""