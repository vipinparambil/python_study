# Num py  array iteration
import numpy as np

# one dimensional
a = np.arange(1, 10)
for i in a:
    print("i: ", i)

# two dimensional

b = np.array([["vi", "da", "sa"],
              [23, 24, 25],
              [60, 70, 80]])
for i in b:
    print("i : ", i)

# row flattening
for v in b.flatten():
    print("values :", v)

# column flattening
for c in b.flatten(order='F'):
    print("c : ", c)

# nditer
x = np.arange(12).reshape(3, 4)
print(x)
print("---------------")
for i in np.nditer(x):
    print("i : ", i)  # row iter

print("---------------")
for i in np.nditer(x, order='F'):
    print("i : ", i)  # column order

print("---------------")

for i in np.nditer(x, order='F', flags=["external_loop"]):
    print(i)  # print the columns are 1D array

print("-----------")
print("nditer is read only")
print("to write use op_flags = ['readwrite']")

for a in np.nditer(x, op_flags=['readwrite']):
    a[...] = a ** a  # ... represent the cur element

print(x)



