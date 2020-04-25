# print infinite lucas series


def lucas_series():
    yield 2
    a = 2
    b = 1
    i = 0
    while i < 10:
        yield b
        a, b = b, a + b
        i = i+1


for x in lucas_series():
    print(x)
