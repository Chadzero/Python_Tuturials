#!/usr/bin/env python
# Name: 001-Multiples_of_3_and_5.py
#
#            Problem
####################################################
# If we list all the natural numbers
# below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
####################################################

__author__ = 'Chad_Ramey'

import sys


def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print 'Usage: range divisor0 [divisor1, ...]'
        sys.exit(1)

    limit = int(args[0])
    divisors = map(int, args[1:])
    total = 0
    numbers = []

    for x in range(0, limit):
        for y in divisors:
            if x % y == 0:
                numbers.append(x)
                total += x
            else:
                continue
            break

    print "From 0 to %s the sum of numbers divisible by %s: is %d" % (limit, ", ".join(args[1:]), total)
    print "These are the numbers: %s" % " ".join(map(str, numbers))

    return

if __name__ == '__main__':
    main()

    #  Consider switching over to using argparse