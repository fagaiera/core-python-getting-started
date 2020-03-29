p = {1, 2, 3, 4, 5, 6}
print(type(p))

# Empty set
e = set()
print(type(e))

s = set([1, 1, 2, 2, 3, 3, 4, 4])
print(s)

for x in s:
	print(x)

print(3 in s)
s.add(5)
print(s)

s.update([6, 7, 8])
print(s)

s.remove(8)
print(s)

# Shallow Copy 

j = s.copy()
print(j)

# Algebra

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print(a.symmetric_difference(b))

print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))