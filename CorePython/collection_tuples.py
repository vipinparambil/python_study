# Tuple - immutable
t = ("abc", 1, 1.2)
print(t)

# postion
print(t[0])

# length
print(len(t))

# loop
for i in t:
    print(i)

# single item
s = (100,)

print(type(s))

# empty tuple
e = ()

# concat
print(t + (1.2, 4))

# multiply
print(t * 3)

# 2 dimensional
tu = ((1, 2), (3, 4), (5, 6))
print(tu[0][1])

# tuple other format
tt = 1, 2, 3, 4
print(type(tt))


# tuple un packing
def find_minmax(items):
    return min(items), max(items)


lower, upper = find_minmax([10, 2, 3, 17, 23, 12, 7])

print("Lower : " + str(lower))
print("Upper : " + str(upper))

# Unpacking ex-2
(a, (b, (c, d))) = (4, (3, (2, 1)))
print(a)
print(b)
print(c)
print(d)

# Un packing ex -3
# swapping
a = 'Jelly'
b = 'Bean'
a, b = b, a

print(a)
print(b)

# tuple constructor
p = tuple([1, 2, 3, 4, 5])
print(p)

st = tuple("This is string tuple")
print(st)

