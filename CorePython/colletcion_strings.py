# Strings
# length
import math

s = "ABCDEfghijklmnopqrstuvwxyz"
print(len(s))

# concatenation
s = "New" + "Field" + "Land"
print(s)

s = "New"
s += "Field"
s += "Abc"
print(s)

# join
s = ";".join(["New", "Field", "Land"])
print(s)
# split
s = "New;Field;Land"
s = s.split(";")
print(s)

# partitioning
s = "The_string"
print(s.partition("_"))

s = "The_String"

a, _, b = s.partition("_")
print(a)
print(b)

# format
s = "The age of {0} is {1} and {0} is a male".format("das", 21)
print(s)

s = "The age of {} is {}".format("vipin", 33)
print(s)

s = "The age of {name} is {age} and {name} is a {sex}".format(name='Vipin', age=22, sex='male')
print(s)

s = "The age of {user[0]} is {user[1]}".format(user=('Vipin', 22))
print(s)

s = "Math constants pi : {m.pi} , e : {m.e}".format(m=math)
print(s)

# decimal precision
s = "Math constats Pi = {m.pi:.3f} E = {m.e:.3f}".format(m=math)
print(s)

value = 4 * 20

s = "The value is {value}".format(value=value)
print(s)

# f-strings

s = f"The values is {value}"
print(s)

import datetime

s = f"The time  is {datetime.datetime.now().isoformat()}"
print(s)

s = f"The math constants pi = {math.pi:.3f} and e = {math.e:.3f}"
print(s)
