# generator comprehensive


# genral syntax
# (expr(item) for item in iterable)


# example
million_squares = (x*x for x in range(1, 1000001))
million_squre_list = list(million_squares)[-10:]
print(million_squre_list)

