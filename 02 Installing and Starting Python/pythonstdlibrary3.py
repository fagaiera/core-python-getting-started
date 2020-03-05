from math import factorial as fac

n = 5
k = 3
print(fac(n)/(fac(k)*fac(n-k)))
print(fac(n)//(fac(k)*fac(n-k)))
print(fac(13) > 2**31 -1)

n = 100
print(len(str(fac(n))))

