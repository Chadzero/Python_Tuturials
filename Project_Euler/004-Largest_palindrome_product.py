#!/usr/bin/env python
# Name: 004-Largest_palindrome_product
# Auther: cRamey
#
#            Problem
####################################################
# A palindromic number reads the same both ways.  The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
####################################################


import sys

def ispalindrome(num):
    middle_index = len(str(num)) / 2
    if len(str(num)) % 2 != 0:
        return str(num)[0:middle_index] == str(num)[-1:middle_index:-1]
    else:
        return str(num)[0:middle_index] == str(num)[-1:middle_index - 1:-1]

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print 'Usage: xxx.py palindrome_divisor_length'
        sys.exit(1)
    pali_div_length = int(args[0])

    #generate maximum length integer
    max_divisor = 10 ** pali_div_length - 1

    max_pali = 0

    for guess in range(max_divisor, 0, -1):
        for guess2 in range (guess, 0, -1):
            product = guess * guess2
            if ispalindrome(product) and product > max_pali:
                max_pali = guess * guess2
                div1 = guess
                div2 = guess2

    print  "The highest product is %s with divisors %s, %s" % (max_pali, div1, div2)
    return max_pali




if __name__ == '__main__':
    main()

'''
Misunderstood the problem and wrote a backwards script

import sys

def make_pali_pair(right_pair):
    return right_pair[::-1]

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print 'Usage: .py palidrome_pair_length'
        sys.exit(1)

    #need to condition numbers so larger than the min needed

    pali_length = int(args[0])

    right_number = 1
    highest_product = 0


    while len(str(right_number)) <= pali_length:

        right_pair = format(right_number, '0' + str(pali_length))
        left_pair = make_pali_pair(right_pair)

        pali_product = right_number * int(left_pair)

        if pali_product > highest_product:
            highest_product = pali_product
            prod_right_pair = right_pair
            prod_left_pair = left_pair
        right_number += 1

    print "%s is the highest product from %s%s" % (pali_product, prod_left_pair, prod_right_pair)
    return pali_product
'''