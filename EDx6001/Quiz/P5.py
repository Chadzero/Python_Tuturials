__author__ = 'Chad_Ramey'


def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    new_string = ''
    for pos, letter in enumerate(s1):
        if pos < len(s2):
            s2_letter = s2[pos]
        else:
            s2_letter = ''
        new_string += s1[pos] + s2_letter
    if len(s2) > len(s1):
        new_string += s2[len(s1):]
    return new_string

# print laceStrings('1234', '12345678')
# print laceStrings('1234777', '123')