# iter() and next() example


def iterate(it):
    iterator = iter(it)
    try:
        return next(iterator)
    except StopIteration as e:
        raise ValueError("Iteration stopped")

lti = ["1", "2", "3"]
print(iterate(lti))
print(iterate(lti))
print(iterate(["1", "2", "3"]))
print(iterate(set()))
