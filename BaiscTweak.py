__author__ = 'Nissanka'

# circuit with single gate for now
import random

def forwardMultiplyGate(x, y):
  return x * y

#some input values
x = -2
y = 3

#try changing x,y randomly small amounts and keep track of what works best
tweak_amount = 0.01
best_out = float('-inf')
best_x = x
best_y = y
for i in range(100):
    x_try = x + tweak_amount * (random.random() * 2 - 1); #tweak x a bit
    y_try = y + tweak_amount * (random.random() * 2 - 1); #tweak y a bit
    out = forwardMultiplyGate(x_try, y_try)
    if(out > best_out):
    # best improvement yet! Keep track of the x and y
        best_out = out
        best_x = x_try
        best_y = y_try

print best_out
print best_x
print best_y
