__author__ = 'Chad_Ramey'

# We can use the idea of bisection search to determine if a character is in a string, so long as the string
# is sorted in alphabetical order.
#
# First, test the middle character of a string against the character you're looking for (the "test character").
# If they are the same, we are done - we've found the character we're looking for!
#
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is aStr. char
# will be a single character and aStr will be a string that is in alphabetical order.  The function should return
# a boolean value.

def isIn(char, aStr):
    '''
    :param char: a single character
    :param aStr: an alphabetized string
    :return: True if char is in aStr; False otherwise
    '''

    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr == char

    midPt = len(aStr) // 2
    if char == aStr[midPt]:
        return True
    elif char < aStr[midPt]:
        aStr = aStr[:midPt]
    else:
        aStr = aStr[midPt:]
    return isIn(char, aStr)
