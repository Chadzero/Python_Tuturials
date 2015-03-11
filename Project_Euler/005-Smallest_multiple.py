#!/usr/bin/env python
# Name: 005-Smallest_multiple
# Auther: cRamey
#
#            Problem
####################################################
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
####################################################

# This should probably be redone using generators

import sys
import operator

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print 'Usage: xxx.py max_divisor'
        sys.exit(1)
    max_divisor = int(args[0])

    divisors = range(max_divisor, 1, -1)
    # need to sort out numbers that we don't need here.  Maybe we can use the prime factor?

    # find the greatest common mulitple
    gcm = reduce(operator.mul, divisors)
    # create range of highest divisor factors
    multiples_highest_divisor = map(lambda x: x * divisors[0], xrange(1, gcm / divisors[0] + 1))
    for multiple in multiples_highest_divisor:
        # create list of factors for all divisors
        if all(y == 0 for y in [multiple % x for x in divisors[1:]]):
            print "The least common denominator is %s" % multiple
            break

    return

if __name__ == '__main__':
    main()
