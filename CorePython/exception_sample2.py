# raise exception

from math import log
from exception_start import convertex2


def logvalue(s):
    x = convertex2(s)
    print(f"log is  : {log(x):0.3f}")


logvalue("one two three".split())  # success
logvalue("abc one two three".split())  # fail
