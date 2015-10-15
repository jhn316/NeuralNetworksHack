__author__ = 'Nissanka'
'''Calculate using analytical experssion for gradient'''

from forwardMultiplyGate import *

x = -2
y = 3
step_size = 0.01
out = forwardMultiplyGate(x, y); # before: -6

x_gradient = y; # by our complex mathematical derivation above
y_gradient = x;

x += step_size * x_gradient; # -2.03
y += step_size * y_gradient; # 2.98
out_new = forwardMultiplyGate(x, y); # -5.87. Higher output! Nice.

print out_new