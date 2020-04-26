# file IO and resource management

# open()
# args to open()
    # file path
    # mode: r, w ,a ,binary or text eg: wt - (write text file),  rb - reab binary etc.
    # encoding

# default encoding
import sys


print(sys.getdefaultencoding())
# open a file for writing
f = open("wasteland.txt", mode="wt", encoding="utf-8")

# write to file
f.write("What are the clutches \n")
f.write("Its not that you \n")
f.write("This is the end\n")
f.close()

# read the file
g = open("wasteland.txt", mode="rt", encoding="utf-8")
# read
print(g.read())
print(g.read())
print(g.read())
print(g.read()) # empty string

g.seek(0) # move to the top position - seek only accept 0 or no retun by tell() method of file

print(g.readline())
print(g.readline())
print(g.readline())
print(g.readline())

g.seek(0)

all_lines = g.readlines()

print(all_lines)
g.close()

# append to the file
a = open("wasteland.txt", mode="at", encoding="utf-8")
lines = ["Append Test \n",
         "The line is appended",
         "This will come in the same line"]
a.writelines(lines)
a.close()


