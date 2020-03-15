urls = {'Google': 'www.google.com', 'Microsoft': 'www.microsoft.com'}
print(urls['Google'])

names_and_ages = [('Alice', 32), ('Bob', 48)]
d = dict(names_and_ages)
print(d)

d = dict(a=123,b=456)
e = d.copy()
print(e)

f = dict(e)
print(f)

for key in urls:
	print(f"{key} => {urls[key]}")

for value in urls.values():
    print(value)

for key, value in urls.items():
    print(f"{key} => {value}")    	

print('Amazon' in urls)    