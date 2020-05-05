# Range
# with stop
for i in range(5):
    print(i)  # print 0,1,2,3,4

# with start and stop
for i in range(5, 10):
    print(i)  # print 5,6,7,8,9

# with start , stop, steps
for i in range(10, 20, 2):
    print(i)

# create list
n = list(range(10, 15))
print(n)

# enumerate
for t in enumerate(n):
    print(t)

for i, v in enumerate(n):
    print(f"The index : {i} and the value : {v}")
