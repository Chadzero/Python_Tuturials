#!/usr/bin/env python
# Name: 001-Multiples_of_3_and_5.py
# Auther: cRamey
#            Problem
####################################################
# Each new term in the Fibonacci sequence is generated by adding the previous two terms
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
####################################################

import sys

def fibGen():
    a, b = 0, 1
    yield 0
    while True:
        a, b = b, a + b
        yield a

def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print 'Usage: limit divisor'
        sys.exit(1)

    limit = int(args[0])
    divisor = int(args[1])
    fibnum = []
    fib = fibGen()

    while True:
        value = next(fib)
        if value >= limit:
            break
        fibnum.append(value)

    print sum(filter(lambda y: y % divisor == 0, fibnum))
    return

if __name__ == '__main__':
    main()

    #  Consider switching over to using argparse