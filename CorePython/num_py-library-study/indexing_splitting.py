# indexing

import numpy as np

a = np.arange(11) ** 2
print(a)
b = a[0:11:2]  # sub array containing elements with index 0 ,2 , 4 etc
print(b)

c = a[::-1]
print(c)  # reverse the array

# multidimensional array

ab = np.arange(12).reshape(3, 4)
print(ab)

c1 = ab[0][1]
print(c1)

c2 = ab[0:2, 1:3]  # 0-2 rows , 1-3 columns
print(c2)
c3 = ab[:, 1:3]
print(c3)

cl = ab[-1, :]  # last row with all columns
print(cl)

cb = ab[-3:-1, -1]
print(cb)

cv = ab[0, ...]  # first row with all columns
print(cv)

cn = ab[..., 1]  # all rows with second column
print(cn)

# slicing
x = np.arange(9)
print("----slice x in to 3 equal arrays - print(np.split(x, 3))")
print(np.split(x, 3))

print("----slice x in to arrays give posItions- print(np.split(x, [4,7])")
print(np.split(x, [4, 7]))

print("---- x ---------")
x = np.array([["Germany", "France", "Hungary", "Austria"],
              ["Berlin", "Paris", "Budapest", "Vienna"]])

print("----slice x HORIZONTALLY - np.hsplit(x, 2)" )
h1, h2 = np.hsplit(x, 2)
print("h1: ", h1)
print("h2 : ", h2)

print("----slice x VERTICALLY - np.vsplit(x, 2)" )
v1, v2 = np.vsplit(x, 2)
print("v1: ", v1)
print("v2 : ", v2)

print("-------shallo copy : x.view()")
s = x.view()

print("---------------deep copy : x.copy()")
d = x.copy()