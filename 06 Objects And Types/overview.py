a = 500
print(id(a))

b = 1000
print(id(b))

b = a
print(id(a) == id(b))

# Equality of Identity
print(a is b)
print(a is None)

# Mutable Objects
r = [2,4,6]
s = r
print(s is r)

s[2] = 8

print(r)


# Value vs Equality of Identity
p = [1,2,3]
q = [1,2,3]
print(p == q)
print(p is q)