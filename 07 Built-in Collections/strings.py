print(len("Hello, World."))
print("a" + "b" + "c")

fruits =';'.join(["apple","banana","pear"])
print(fruits)

print(fruits.split(';'))

print("unforgetable".partition('forget'))

departure, separator, arrival = 'London:Edinburgh'.partition(':')
print(departure)
print(arrival)

#Formatting
a = "The age of {0} is {1}".format("John",32)
print(a)

#F-strings

a = f'The value is {3*4}'
print(a)