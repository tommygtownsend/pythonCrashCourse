# =======================================
# Lambda Functions
# =======================================
# https://www.w3schools.com/python/python_lambda.asp
# A lambda function is a small, anonymous function.
# It’s like a “throwaway” function you don’t need to name.
#
# In normal Python, we’d define a function like this:
def square(x):
    return x * x
print("Square (normal):", square(5))

# With lambda, we can do the same in one line:
square_lambda = lambda x: x * x
print("Square (lambda):", square_lambda(5))

# Syntax: lambda arguments: expression
# Note: Lambdas can only contain one expression (no loops or statements inside).
# Useful when you just need a quick function once.


# =======================================
# Lambda Practice !!!
# =======================================
# Try making a lambda that doubles a number,
# then call it on an int like 10 and print the result!









# =======================================
# Higher-Order Functions
# =======================================
# A higher-order function is a function that either:
#   1. Takes another function as input
#   2. Returns a function as output
#
# Python has several built-in higher-order functions.
# The most common ones are map(), filter(), and reduce().

# Example 1: map()
# map(function, iterable) applies a function to every element.
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, nums))
print("Squared with map:", squared)

# Example 2: filter()
# filter(function, iterable) keeps only items where function returns True.
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers with filter:", evens)

# Example 3: reduce()
# reduce(function, iterable) “reduces” the iterable into a single value.
from functools import reduce
sum_all = reduce(lambda x, y: x + y, nums)
print("Sum with reduce:", sum_all)


# =======================================
# Higher-Order Functions Practice !!!
# =======================================
# 1. Use map() with a lambda to triple each number in nums.
# 2. Use filter() with a lambda to get numbers greater than 2.
# 3. Use reduce() with a lambda to multiply all numbers in nums.
# Print your results!






# =======================================
# Passing Functions Around
# =======================================
# We can also pass named functions into higher-order ones.
def is_odd(x):
    return x % 2 != 0

odds = list(filter(is_odd, nums))
print("Odd numbers (named function):", odds)


# =======================================
# Functions Returning Functions
# =======================================
# A higher-order function can return a new function.

def make_multiplier(n):
    # returns a lambda function that multiplies by n
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double 5:", double(5))
print("Triple 5:", triple(5))


# =======================================
# Functions Returning Functions Practice
# =======================================
# Create a make_adder(n) function that returns a lambda which adds n.
# Then make add5 = make_adder(5) and show that add5(10) == 15.
