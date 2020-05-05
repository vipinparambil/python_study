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
