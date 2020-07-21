# Sample Equations
#
# Description: Sample functions (and their derivatives)
# to be used with the root-finding algorithms.
#

#Equation 1
def eq1(x):
    return x**5 - 5*x + 1

def eq1_d(x):
    return 5*(x**4) - 5

# Equation 2
def eq2(x):
    return (pow(x, 2) - 4)

def eq2_d(x):
    return 2*x