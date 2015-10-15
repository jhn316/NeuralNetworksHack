__author__ = 'Nissanka'

'''Check results of BackPropBasic using Numerical model'''
# initial conditions
x = -2
y = 5
z = -4

def forwardMultiplyGate(a, b):
    return a * b

def forwardAddGate(a, b):
    return a + b

def forwardCircuit(x,y,z):
    q = forwardAddGate(x, y)
    f = forwardMultiplyGate(q, z)
    return f

# numerical gradient check
h = 0.0001
x_derivative = (forwardCircuit(x+h,y,z) - forwardCircuit(x,y,z)) / h # -4
y_derivative = (forwardCircuit(x,y+h,z) - forwardCircuit(x,y,z)) / h # -4
z_derivative = (forwardCircuit(x,y,z+h) - forwardCircuit(x,y,z)) / h # 3

print x_derivative
print y_derivative
print z_derivative

