import os
import time
from math import sqrt

#   Recursion tree with n depth running time
#   Base: n = 1 --> O(1)
#   Assume T(n-1) = O(2n-1), therefore
#   T(n) = T(n-1) + T(n-2) + O(1) which is equal to
#   T(n) = O(2^n-1) + O(2^n-2) + O(1) = O(2^n)
#   Running time is O(2^n)

#         _
#        |   0           if n=0
#        |
#F(n) = -    1           if n=1
#        |
#        |   Fn-1 +Fn-2  if n>1
#         -


def fib_formula(n):
    # it uses phi math formula
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))


def fib(n):
    # recursevely calculates fibonacci sequence
    # using test cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_seq(n):
    # prints the sequence with elements
    for i in range(n+1):
        print i, "\t->\t", fib(i)


def main():

    os.system('clear')

    print "\n\t Fibonnaci sequence\n"
    elements = input("Enter a positive number of elements: ")
    
    
    start = time.time()                             # stores the starting time
    fibonacci_formula = fib_formula(elements)       # call fibonacci sequence recursevelly
    stop = time.time()                              # stores the stoping time
    fibonacci_formula_timing = stop - start
    print "\n(FORMULA)Fibonacci number on nth", elements,"element position is", fibonacci_formula
    print "In ",fibonacci_formula_timing, "seconds"


    start = time.time()             # stores the starting time
    fibonacci = fib(elements)       # call fibonacci sequence recursevelly
    stop = time.time()              # stores the stoping time
    fibonacci_timing = stop - start
    print "\n(RECURSEVELY)Fibonacci number on nth", elements,"element position is", fibonacci
    print "In ",fibonacci_timing, "seconds"
    

    print "\n(RECURSEVELY)Full sequence from given number of elements: \nelement -> sequence"
    start = time.time()             # stores the starting time
    fib_seq(elements)               # call fibonacci sequence recursevelly
    stop = time.time()              # stores the stoping time
    fibonacci_sequence_timing = stop - start
    print "In ",fibonacci_sequence_timing, "seconds"

if __name__=="__main__": main()














