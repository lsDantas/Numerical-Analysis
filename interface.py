# Text Interface
#
# Description: A simple text interface for using the 
# root-finding algorithms.
#

from bisection_method import *
from newton_method import *
from sign import *
from sample_equations import *

# Select algorithm prompt
print("Root-finding algorithms\n\n"
       + "(1) Bisection Method\n"
       + "(2) Newton's Method\n")
method_num = float(input("Select an algorithm: "))
while method_num != 1 and method_num != 2:
    method_num = float(input("Unavailable option. Select an algorithm: "))

# Select equation prompt
print("\nAvailable Equations\n\n"
          + "(1) x^5 - 5x + 1\n" 
          + "(2) x^2 - 4\n")
eq_num = float(input("Select an equation: "))
while eq_num != 1 and eq_num != 2:
    eq_sum = float(input("Unavailable option. Select an equation: "))

# Run methods
if method_num == 1:
    # Bisection Method

    # Gather parameters
    a = float(input("\nInitial left bound: "))
    b = float(input("Initial right bound: "))
    min_inter = float(input("Minimum interval size (halt criterion): "))
    max_iter = float(input("Maximum number of steps: "))

    # Run bisection algorithm
    if eq_num == 1:
        a, b, counter = bisection_method(eq1, a, b, min_inter, max_iter)
    else:
        a, b, counter = bisection_method(eq2, a, b, min_inter, max_iter)
    
    # Display Results
    print("\nInterval: [ {}, {}]".format(a,b))
    print("Number of steps required: {}".format(counter))
else: 
    # Newton's Method 

    # Gather Parameters
    x0 = float(input("Initial guess: "))
    precision = float(input("Precision: "))
    max_iter = float(input("Maximum number of steps: "))

    # Run Newton's algorithm
    if eq_num == 1:
        x, counter = newton_method(eq1, eq1_d, x0, precision, max_iter)
    else:
        x, counter = newton_method(eq2, eq2_d, x0, precision, max_iter)

    # Display Results
    print("\nApproximate root: {}".format(x))
    print("Number of steps required: {}".format(counter))
