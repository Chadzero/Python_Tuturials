__author__ = 'Chad_Ramey'

# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every
# other element of the input tuple is copied, starting with the first one

def oddTuples(aTup):
    '''
    :param aTup: a tuple
    :return: tuple, every other element of aTup
    '''

    return aTup[::2]

print oddTuples((0,1,2,3,4))