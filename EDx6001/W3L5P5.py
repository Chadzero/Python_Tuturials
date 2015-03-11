__author__ = 'Chad_Ramey'

# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b
#  are two positive integers: if b = 0, then the answer is a. Otherwise Otherwise, gcd(a, b) is the same
#  as gcd(b, a % b)

def gcdRecur(a, b):
    '''
    :param a: positive integer
    :param b: positive integer
    :return: a positive integer, the greatest common divisor of a & b
    '''

    # order the numbers so a is largest int
    if b > a:
        a, b = b, a

    if b == 0:
        return a

    return gcdRecur(b, a % b)