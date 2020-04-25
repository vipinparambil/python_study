# comprehension with filter

from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False;
    return True;


def main():
    # filter
    primes = [x for x in range(100) if is_prime(x)]
    print(primes)
    prime_square = {x * x: (1, x, x*x) for x in range(20) if is_prime(x)}
    print(prime_square)


if __name__ == '__main__':
    main()
