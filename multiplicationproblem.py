# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def multiplicationproblem(a,b):
    c = a*b
    if c <= 1000:
        return c
    else:
        return a+b


a = int(input('Enter first number'))
b = int(input('Enter second number'))
z = multiplicationproblem(a,b)
print("Output: ",z )