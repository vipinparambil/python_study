# generator example
# used to create iterables


def gen123():
    yield '1'
    yield '2'
    yield '3'


g = gen123()

print(g)  # print <generator object gen123 at 0x7f57e7ab0660>

print(next(g))  # print 1
print(next(g))  # print 2
print(next(g))  # print 3
# print(next(g))  # StopIteration exception

h = gen123()

print(f" h is  g : {h is g}")


def gen456():
    print("Yield : 1")
    yield '1'
    print("Yield : 2")
    yield '2'
    print("Yield : 3")
    yield '3'


g = gen456()

print(next(g))
print(next(g))
print(next(g))

for x in gen123():
    print(x)