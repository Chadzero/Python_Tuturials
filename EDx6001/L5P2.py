__author__ = 'Chad_Ramey'

# In Problem 1, we computed an exponential by iteratively executing successive multiplications. We can use the same
# idea, but in a recursive function.
# Write a function recurPower(base, exp) which computes baseexp by recursively calling itself to solve a smaller
# version of the same problem, and then multiplying the result by base to solve the initial problem.


def recurPower(base, exp):
    '''

    :param base: int or float
    :param exp: int >= 0
    :return: int or float, base^exp
    '''

    if exp == 0:
        return 1
    return(base * recurPower(base, exp - 1))