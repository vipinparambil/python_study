# Demo for exception
import sys

DIGIT_MAP = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}


# without exception handling
def convert(s):
    number = ""
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x


# print(f"number : {convert('around one two three'.split())}")  # raise key error

# conversion with exception handling


def convertex1(s):
    x = -1
    try:
        number = ""
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion success")
    except (KeyError, TypeError) as e:
        pass  # for empty block
    return x


#print(f"number : {convertex1('around one two three'.split())}")  # key error

#print(f"number : {convertex1(517)}")  # Type Error

#print(f"number : {convertex1('one two three'.split())}")


def convertex2(s):
    x = -1
    try:
        number = ""
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("Conversion success")
    except (KeyError, TypeError) as e:
        print(f"Conversion error {e!r}", file=sys.stderr) # print the exception with more details to std error console
        raise
    return x


#print(f"number : {convertex2(517)}")  # Type Error
