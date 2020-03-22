def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

g = gen246()
print(next(g))
print(next(g))
print(next(g))
print(next(g))