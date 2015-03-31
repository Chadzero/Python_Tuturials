__author__ = 'Chad_Ramey'

# For each of the following questions (which you may assume is evaluated independently of the previous questions, so
# that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation
# testList has the indicated value. You may need to write a simple procedure in each question to help with this process.


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1