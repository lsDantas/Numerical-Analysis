# Newton Method
#
# Description: Implements Newton's root-finding
# algorithm for real-valued functions.
#
# Inputs
#   func:      a function of a real number x 
#              (implemented as a Python function)
#   func_d:    the derivative of func
#              (implemented as a Python function)
#   x0:        initial guess for root
#   precision: desired distance from zero
#              (halt criterion)
#   max_iter:  maximum number of iterations
#
# Outputs
#   x1:      approximate root
#   counter: number of iterations required
#

def newton_method(func, func_d, x0, precision, max_iter = 1000):
    # Perturbation to prevent divisions by zero
    h = 0.00000001
    
    # Cap maximum amount of iterations
    counter = 1
    while(counter <= max_iter):
        # Check for null derivative at x0
        if(func_d(x0) == 0):
            # Add perturbation
            x1 = x0 - func(x0)/(func_d(x0) + h)
        else:
            # General case
            x1 = x0 - func(x0)/func_d(x0)

        # Check if desired precision reached
        if(abs(func(x1) - 0) < precision):
            return x1, counter
        else:
            # Update x
            x0 = x1
        
        # Update counter
        counter = counter + 1

    return x1, counter