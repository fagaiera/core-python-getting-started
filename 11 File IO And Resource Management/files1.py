import sys

print(sys.getdefaultencoding())

f = open("wasteland.txt", mode = "wt", encoding = "utf-8")
f.write("What are the roots that clutch, ")
f.write("What branches grow\n")
f.write("Out of this stony rubbish? ")
f.close()

g = open("wasteland.txt", mode = "rt", encoding = "utf-8")
print(g.read(32))
print(g.read())
print(g.read())

print(g.seek(0))
print(g.readline())
print(g.readline())
print(g.seek(0))

print(g.readlines())
g.close()


h = open("wasteland.txt", mode = "at", encoding = "utf-8")
h.writelines(
            ["Son of man, \n",
             "You cannot say, or guess, ",
             "for you only, \n",
             "A heap of broken images, ",
             "where the sun beats\n"])

h.close()
