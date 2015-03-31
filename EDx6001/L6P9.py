__author__ = 'Chad_Ramey'


# We are now going to evaluate a aset of expression, resulting in the following sequence of interactions. Fill in each
# blank to show what the Python interpreter would print at that point.


animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

print animals

print animals['c']

# print animals['donkey']

print len(animals)

animals['a'] = 'anteater'
print animals['a']

print len(animals['a'])

print animals.has_key('baboon')

print 'donkey' in animals.values()

print animals.has_key('b')

print animals.keys()

del animals['b']
print len(animals)

print animals.values()