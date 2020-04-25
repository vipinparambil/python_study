from pprint import pprint as pp

# Dictionary
d = {"H": 12, "M": 14, "Li": 28, "Lh": 30}

# pp example
pp(d)

# Dictionary constructor
la = [("H", 12), ("M", 14), ("Li", 28), ("Lh", 30)]
di = dict(la)
print(di)

diw = dict(a="abc", b="cde", c="fgh")
print(diw)

# iteration
for i in d:
    print(f"key => {i} , value => {d[i]}")
# keys
for k in d.keys():
    print(f"key => {k}")

# values
for v in d.values():
    print(f"Value => {v}")

# items
for k, v in d.items():
    print(f"key => {k} , value => {v}")

# update
di.update(diw)
print(di)

di['H'] += 2
print(di)

# delete
del di['a']
pp(di)
