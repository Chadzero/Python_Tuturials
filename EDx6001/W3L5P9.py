__author__ = 'Chad_Ramey'

# A semordnilap is a word or a phrase that spells a different word when backwards
# Write a recursive program, semordnilap, that takes in two words and says if they are semordnilap.
# Do an input check to ensure words are not single characters or equal

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''

    if len(str1) == 1 or len(str2) == 1:
        return str1 == str2

    if str1[0] != str2[-1]:
        return False

    return semordnilap(str1[1:], str2[:-1])



def semordnilapWrapper(str1, str2):
    # check inputs  are not single character
    if len(str1) + len(str2) <= 2 or len(str1) != len(str2):
        return False

    # check inputs are not the same
    if str1 == str2:
        return False

    return semordnilap(str1, str2)