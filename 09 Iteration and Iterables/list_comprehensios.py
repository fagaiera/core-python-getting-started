words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
print([len(word) for word in words])

lengths = []
for word in words:
	lengths.append(len(word))
print(lengths)