__author__ = 'Chad_Ramey'

# The greatest common divisor of two positive integers is the largest integer that divides each of them
# without remainder.
#
# Write an iterative function, gcdIter(a, b), that implements this idea.

def gcdIter(a, b):
    '''
    :param a: positive integer
    :param b: positive integer
    :return: a positive integer, the greatest common divisor of a & b
    '''

    if a > b:
        start = b
    else:
        start = a

    while start > 0:
        if a % start == 0 and b % start == 0:
            break
        else:
            start -= 1
    return start