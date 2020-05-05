# numpy array creation sample
import sys

import numpy as np

a1 = np.array([1, 2, 3, 4])
print(a1)

a2 = np.array([(1, 2), (2, 3)])
print(a2)

# zeros

zero_a = np.zeros((3, 3))
print(f"3 X 3 zero matrix :\n {zero_a}")

# ones
ones_a = np.ones((3, 3), dtype=np.int16)
print(f"3 X 3 ones matrix :\n {ones_a}")

# empty
empty_a = np.empty((3, 3))
print(f"3 X 3 empty matrix :\n {empty_a}")

# digonal 1
eye_A = np.eye(3)
print(f"3 X 3 digonal one matrix  : \n {eye_A}")

# range
arrange_1 = np.arange(3)
print(arrange_1)

evn_num = np.arange(2, 20, 2)
print(f"evn numbers upto 20  : \n {evn_num}")

array_floats = np.arange(1, 5, 0.3)
print(array_floats)  # increment by 0.3

# shape - row X column
print(eye_A.shape)

# reshape - reshape to given r X c
re_a = np.arange(6)
re_shape_a = re_a.reshape(3, 2)
print(re_shape_a)

# ones like - create array with one
re_ones = np.ones_like(re_shape_a)
print(re_ones)

# set conf for printing np
np.set_printoptions(threshold=sys.maxsize)  # print all elements to console

print(np.arange(1000))

