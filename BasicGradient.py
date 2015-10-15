__author__ = 'Nissanka'

'''Basic gradient'''
from forwardMultiplyGate import *

x = -2
y = 3
h = 0.0001
step_size = 0.01
out = forwardMultiplyGate(x, y) # before: -6

# compute derivative with respect to x
xph = x + h # -1.9999
out2 = forwardMultiplyGate(xph, y) # -5.9997
x_derivative = (out2 - out) / h # 3.0

# compute derivative with respect to y
yph = y + h # 3.0001
out3 = forwardMultiplyGate(x, yph) # -6.0002
y_derivative = (out3 - out) / h # -2.0


x = x + step_size * x_derivative # x becomes -1.97
y = y + step_size * y_derivative # y becomes 2.98
out_new = forwardMultiplyGate(x, y) # -5.87! exciting.

print out_new
