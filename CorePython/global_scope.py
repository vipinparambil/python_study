count = 0


def show_count():
    print(count)


def set_count(c):
    count = c


show_count()

# set count
set_count(5)

# display count  as 0
show_count()


def set_global_count(c):
    global count
    count = c


set_global_count(10)

show_count()
