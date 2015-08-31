__author__ = 'Chad_Ramey'


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if x < b:
        return 0
    return myLog(x-b, b) + 1

print myLog(16, 2)