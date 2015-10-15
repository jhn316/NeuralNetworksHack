__author__ = 'Nissanka'

'''Implements recursive NN with add and multiply '''
def forwardMultiplyGate(a, b):
    return a * b

def forwardAddGate(a, b):
    return a + b

def forwardCircuit(x,y,z):
    q = forwardAddGate(x, y)
    f = forwardMultiplyGate(q, z)
    return f

x = -2
y = 5
z = -4
f = forwardCircuit(x, y, z) # output is -12

print f
