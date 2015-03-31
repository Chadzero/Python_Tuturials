#!/usr/bin/env python
# Name: 003-Largest_prime_factor.py
# Auther: cRamey
#            Problem
####################################################
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?.
####################################################


# Get a number
# Check if number is int factor
# if factor check if number is prime

import sys

def isprime(guessnum):
    result = True
    for divisor in range(2, guessnum / 2):
        if float(guessnum) % float(divisor) == 0:
            result = False
    return result

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print 'Usage: .py upper_limit'
        sys.exit(1)

    #need to condition numbers so larger than the min needed
    upper_limit = long(args[0])

    result = "There are no factors.  You're number is prime"

    for num in range(3, upper_limit / 2, 2):
        if isprime(num):
            result = "The largest prime factor is %s" % num

    print result
    return

if __name__ == '__main__':
    main()

    #  Consider switching over to using argparse
