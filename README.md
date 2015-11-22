tidbits
=======

A repo of small projects or snippets that don't fit anywhere else.

##Projects

 - CollabFilter.scala
    - A naive collaborative filter in scala
 - codecombat.js
    - My solution to the problem posed in http://blog.codecombat.com/having-your-algorithms-ass-kicked-by-the-internet
    - gets 30 rectangles in some number of statements
 - collab.py
    - Naive collaborative filtering in python
    - this got me started on some larger projects you can see elsewhere (ClassRank)
 - compiler_3.py
    - brainfuck interpreter implemented as a final project for my CS101 course
    - I might go back and codegolf this now
 - importmagic.py, importtester.py
    - a fun side project to break python
    - importmagic is a file that allows you to import any function defined in the importing file
    - the idea was to use this as a frontend for some kind of typechecking or mokeypatching library
    - one would use `from thing import [list of functions to monkeypatch]`
 - lispy.py
    - a semi-golfed lisp implementation a friend and I built
    - the parser-tokenizer is a single line regex that converts the lisp text into json text
    - this text is then json.loaded into a python dictionary
    - because of the way its written, you can then import python modules (like math) and use builtins
 - obiwan_extras.py
    - an addon to the obiwan module (https://pypi.python.org/pypi/obiwan/1.0.2)
    - adds some syntactic sugar, reimplements some things
    - inspired by/deals with things like the proposals to do type hinting in python
    - specifically, I dislike mypy's proposed syntax
    - https://quip.com/r69HA9GhGa7J
 - overloading.py
    - one of my first runs into python's cool stuff (decorators)
 - quicksortShort.py
    - variants on codegolfed quicksort algorithms
