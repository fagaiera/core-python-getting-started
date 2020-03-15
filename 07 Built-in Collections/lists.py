r = [1, 2, 3, 4, 5, 6]
print(r[-1])
print(r[-2])

#Slicing

print(r[1:3])
print(r[:])

#Copy
s = r[:]
print(s is r)
print(s == r)


u = s.copy()
print(u is s)
print(u == r)

v = list(s)
print(v is s)
print(v == r)

print("")
a = [[1, 2], [3, 4]]
b = a[:]
print(a is b)
print(a == b)
print(a[0] is b[0])

c = [21, 32]
d = c * 4
print(d)

s = [[-1, 1]] * 4
s[2].append(4)
print(s)

w = "the quick brown fox jumps over the lazy dog".split()	
print(w)
i = w.index('fox')
print(i)
print(w.count('the'))

w = [1, 2, 3, 4, 5, 6]
print(32 in w)
print(32 not in w)

#Delete

u = "jackdaws love my sphinx of quartz".split()
print(u)
del(u[3])
print(u)

u.remove('jackdaws')
print(u)


#Insert

a = "I accidentally the whole universe".split()
print(a)
a.insert(2, "destroyed")
' '.join(a)
print(a)


#Concatenate

m = [1, 2, 3]
n = [4, 5, 6]
k = m + n
print(k)
k.extend([7, 8, 9])
print(k)

#Reverse

a = [1, 2, 3]
a.reverse()
print(a)

d = [17, 41, 29]
d.sort()
print(d)

d.sort(reverse=True)
print(d)




h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
print(h)
h.sort(key=len)
y = ' '.join(h)
print(y)








