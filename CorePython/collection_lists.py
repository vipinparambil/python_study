# List

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l)

# negative index
# -1 print last element
print(l[-1])  # print the last element  - 9
print(l[-2])  # print second last element - 8

# slicing - create sub list

l1 = l[1:2]
print(f" L1 : {l1}")

l2 = l[1:-1]
print(f" L2 : {l2}")

l3 = l[2:]
print(f" L3 : {l3}")

l4 = l[:2]
print(f" L4 : {l4}")

# list copy
r = l[:]
print(r)
print(f"The list are same : {r is l}")  # print false
print(f"The list are same : {r == l}")  # print true

u = l.copy()
print(f"The list are same : {u is l}")  # print false
print(f"The list are same : {u == l}")  # print true

v = list(l)
print(f"The list are same : {v is l}")  # print false
print(f"The list are same : {v == l}")  # print true

# shallow copy
a = [[1, 2], [2, 3]]
b = a[:]

print(f"b is a : {b is a}")  # print false

print(f" a[0] is b[0] {a[0] is b[0]}")  # print true

a[0] = [4, 5]
print(a[0])  # [4, 5]
print(b[0])  # [1, 2]

print(a[1])  # [2, 3]
print(b[1])  # [2, 3]

a[1].append(4)
print(a[1])  # [2, 3, 4]
print(b[1])  # [2, 3, 4]

# multiply
c = [2, 1, 4]
d = c * 2
print(d)

# index
w = "the quick brown fox jumps over the lazy dog".split()
i = w.index("brown")
print(i)

c = w.count("the")
print(c)

while "the" in w:
    print("the")
    break;

if "jags" not in w:
    print("not in")

# delete
del w[0]
print(w)

w.remove("the")
print(" ".join(w))

w.insert(0, "the")
print(" ".join(w))

# concat
m = [1, 2, 3, 4]
n = [5, 6, 7]
k = m + n
print(k)

k += [8, 9]
print(k)

k.extend([10, 11, 12])
print(k)

# Reverse and Sort
k.reverse()
print(k)
k.sort()
print(k)
k.sort(reverse=True)
print(k)

h = "not perplexing do handwriting family where i illegibly know doctors".split()
h.sort(key=len)
print(" ".join(h))

r = list(reversed(k))
print(r)

sh = sorted(h, key=len)
print(" ".join(sh).capitalize())





