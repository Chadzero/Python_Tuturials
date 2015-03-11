__author__ = 'Chad_Ramey'

# Write an iterative function, lenIter, which computes the length of an input argument (a string), by counting up the
# number of characters in the string.

def lenIter(aStr):
    '''
    :param aStr: a string
    :return: int, the length of a sStr
    '''
    count = 0
    for c in str(aStr):
        count += 1
    return count