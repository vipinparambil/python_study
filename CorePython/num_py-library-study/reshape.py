# Reshape
import numpy as np

x = np.array([["Germany", "France", "Hungary", "Austria"],
              ["Berlin", "Paris", "Budapest", "Vienna"]])
print("-----------Array-------")
print(x)

print("------------x.shape")
print(x.shape)

print("-------flatten by x.ravel()")
print(x.ravel())

print("--------Transpose : x.T")
print(x.T)

print('--------reshape x.reshape()')
print(x.reshape(2, 4))

country = np.array(["Germany", "France", "Hungary"])
print(" ------x.reshape(-1, 3) - unknown rows , but 3 columns must")
print(country.reshape(-1, 3))

print(" ------x.reshape(3, -1) - unknown columns , but 3 rows must")
print(country.reshape(3, -1))