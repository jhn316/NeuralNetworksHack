__author__ = 'Nissanka'

'''Approximates partial derivative'''
#import forwardMultiplyGate as fMG
from forwardMultiplyGate import *

x = -2 
y = 3
out = forwardMultiplyGate(x, y) # -6
h = 0.0001

# compute derivative with respect to x
xph = x + h # -1.9999
out2 = forwardMultiplyGate(xph, y) # -5.9997
x_derivative = (out2 - out) / h # 3.0

# compute derivative with respect to y
yph = y + h # 3.0001
out3 = forwardMultiplyGate(x, yph) # -6.0002
y_derivative = (out3 - out) / h # -2.0

print x_derivative
print y_derivative
