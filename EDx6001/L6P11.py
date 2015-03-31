__author__ = 'Chad_Ramey'

# We want to write some simple procedures that work on dictionaries to return information.
# This time, write a procedure, called biggest ,  which returns the key corresponding to the entry with the
# largest number of values associated with it. If there is more than one such entry, return any one of the matching keys


def biggest(aDict):
    '''
    :param aDict: A dictionary, where all the values are lists.
    :return: The key with the largest number of values associated with it.
    '''

    biggest_key = None

    for key, value in aDict.items():
        if biggest_key:
            if len(aDict[biggest_key]) >= len(value):
                continue
        biggest_key = key

    return biggest_key







animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')