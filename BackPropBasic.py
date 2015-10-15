__author__ = 'Nissanka'

'''Implements basic backprop'''
# initial conditions
x = -2
y = 5
z = -4

# Define the functions
def forwardMultiplyGate(a, b):
    return a * b

def forwardAddGate(a, b):
    return a + b

q = forwardAddGate(x, y) # q is 3
f = forwardMultiplyGate(q, z) # output is -12

# gradient of the MULTIPLY gate with respect to its inputs
# wrt is short for "with respect to"
derivative_f_wrt_z = q # 3
derivative_f_wrt_q = z # -4

# derivative of the ADD gate with respect to its inputs
derivative_q_wrt_x = 1.0
derivative_q_wrt_y = 1.0

# chain rule
derivative_f_wrt_x = derivative_q_wrt_x * derivative_f_wrt_q # -4
derivative_f_wrt_y = derivative_q_wrt_y * derivative_f_wrt_q # -4

# final gradient, from above: [-4, -4, 3]
gradient_f_wrt_xyz = [derivative_f_wrt_x, derivative_f_wrt_y, derivative_f_wrt_z]


#----backprop. part---
# let the inputs respond to the force/tug:
step_size = 0.01 
x = x + step_size * derivative_f_wrt_x  # -2.04
y = y + step_size * derivative_f_wrt_y  # 4.96
z = z + step_size * derivative_f_wrt_z  # -3.97

# Our circuit now better give higher output:
q = forwardAddGate(x, y)  # q becomes 2.92
f = forwardMultiplyGate(q, z)  # output is -11.59, up from -12! Nice!

print "q = ", q
print "f = ", f