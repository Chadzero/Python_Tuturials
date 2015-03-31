__author__ = 'Chad_Ramey'

# First, write a procedure, called howMany, which returns the  sum of the number of values associated with a dict.


def howMany(aDict):
    '''
    :param aDict: A dictionary, where all the values are lists
    :return: int, how many values are in the dictionary
    '''

    total = 0

    for key in aDict:
        total += len(aDict[key])

    return total


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')