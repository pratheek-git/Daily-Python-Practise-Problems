# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.

def sumofcurrentnumber(number):
    previous_number = 0  # previous  number assigned to zero
    for i in range(number):
        result = i + previous_number
        print(f"Current number {i} Previous number {previous_number} Sum: {result}")
        previous_number = i


number = int(input('Enter a number'))
sumofcurrentnumber(number)