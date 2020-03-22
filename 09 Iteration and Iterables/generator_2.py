def gen123():
    yield 1
    yield 2
    yield 3
    
for v in gen123():
    print(v)

h = gen123()
i = gen123()
print(h is i)