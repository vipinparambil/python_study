# exception raise example
import sys


def sqrt(x):
    """
    Compute square root of using Heron of Alaxandra method
    :param x:
    :return: the square root of x
    """
    if x < 0:
        raise ValueError("Sqrt calculation of negative number is not possible")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    print("Enter number to find square root")
    x = int(input())
    try:
        print(f"Sqrt of {x} is : {sqrt(x)}")
    except ValueError as e:
        print(e, file=sys.stderr)
    finally:
        print("Always finally")


if __name__ == "__main__":
    main()
