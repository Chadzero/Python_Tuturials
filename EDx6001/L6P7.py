__author__ = 'Chad_Ramey'

# For each of the following questions (which you may assume is evaluated independently of the previous questions, so
# that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation
# testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

print applyToEach(testList,abs)

def increment(num):
    return num + 1

print applyToEach(testList, increment)

def sqrd(num):
    return num ** 2

print applyToEach(testList, sqrd)
