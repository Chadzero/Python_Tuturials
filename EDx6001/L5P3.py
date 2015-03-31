__author__ = 'Chad_Ramey'

# Another way to solve this problem just using multiplication (and remainder) is to note that

def recurPowerNew(base, exp):
    '''

    :param base: int or float.
    :param exp: int >= 0
    :return: int or float; base^exp
    '''

    if exp == 0:
        return 1
    elif exp % 2 == 0: # exp is even
        return recurPowerNew(base * base, exp / 2)
    else: # exp is odd
        return base * recurPowerNew(base, exp - 1)