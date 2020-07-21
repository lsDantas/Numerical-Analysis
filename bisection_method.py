# Bisection Method
#
# Description: Implements the bisection method, a 
# root-finding algorithm for continuous functions
# that are known to assume positive and negative
# values
#
# Inputs
#   func:      a function of a real number x 
#              (implemented as a Python function)
#   a:         left bound of search interval
#   b:         right bound of search interval
#   min_inter: minimum interval size (halt criterion)
#   max_iter:  maximum number of iterations
#
#
# Outputs
#   a:       left bound of interval containing root
#   b:       right bound of interval containing root
#   counter: number of iterations required
#

from sign import *

def bisection_method(func, a ,b, min_inter, max_iter=1000):
    counter = 1
    min_inter = abs(min_inter)

    # Cap maximum amount of iterations
    while(counter <= max_iter):
        # Verify if root is exactly on interval bounds
        if(func(a) == 0 and func(a+min_inter) == 0):
            return a, a + min_inter, counter
        if(func(b) == 0 and func(b-min_inter) == 0):
            return b, b - min_inter, counter

        # Take interval midpoint
        midpoint = abs(a+b)/2

        # Check if minimum interval size reached
        if( abs(a - midpoint) < min_inter or abs(midpoint - b) < min_inter ):
            return a, b, counter

        # Adjust appropriate bound, reduce interval
        if(sign(func(a)) == sign(func(midpoint))):
            a = midpoint
        else:
            b = midpoint

        # Update counter
        counter = counter + 1
    
    return a,b, counter