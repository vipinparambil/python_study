# array operations

import numpy as np
# one dimensional array

a = np.array([10, 10, 10])
b = np.array([5, 5, 5])

# arithmetic
print(f" a + b : { a + b}")
print(f" a- b : {a - b}")

print(f" a/ b  : { a/ b}")
print(f"a % 3 : {a % 3}")

print(f"a < 12 : {a < 12}")

a *= 3
print(f" a * 3 : {a}")
b += a
print(b)

ages = np.array([20, 24, 25, 27, 28, 23])

print(f"ages : {ages}")
print(f" sum : {np.sum(ages)}")
print(f"max : {np.max(ages)}")
print(f"min : {np.min(ages)}")


# two dimensional array

a2 = np.array([[2, 3],
               [1, 4]])
b2 = np.array([[1, 0],
               [5, 6]])

c2 = a2 * b2
print(f"element multiplication in matrix : {c2}")

c3 = a2.dot(b2)   # real matrix multiplication
print(f"matrix multiplication : {c3}")

numbers = np.arange(12).reshape(3, 4)
print(numbers)

sum_columns = np.sum(numbers, axis=0)  # sum of each column
print(f"sum co;umns : {sum_columns}")

sum_rows = np.sum(numbers, axis=1)  # sum of each row
print(f"sum of rows : {sum_rows}")

max_row = np.max(numbers, axis=1)  # max of row
print(max_row)


