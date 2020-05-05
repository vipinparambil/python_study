# iteration tools


from core.comprehension_with_fiter import is_prime
from itertools import islice, count

# itertools.islice() - slicing of the iterator
# itertools.count() - infinite series of numbers

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)

for p in list(thousand_primes)[-10:]:
    print(p)

# any
# check any prime no between 1235 and 1789
exist = any(is_prime(x) for x in range(1235, 1789))
print(f"is prime exist {exist}")

# all
all_prime = all(is_prime(x) for x in range(10, 11))
print("all is prime {}".format(all_prime))

# zip -  combine the iterable as tuples
odd_no = [1, 3, 5, 7, 9]
even_no = [2, 4, 6, 8]
for x in zip(odd_no, even_no):
    print(x)

# chain - combine two iterables

from itertools import chain

aa = chain(odd_no, even_no)
for a in aa:
    print(a)
