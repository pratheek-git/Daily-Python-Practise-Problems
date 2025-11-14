# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.
#
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
str = "PYnative"
print("Original string is {}".format(str))
list_fr = list(str.strip())
print("Printing only even index chars:")
for i in range(len(list_fr)): # To do operations in index value use of range(len(list_fr)) is neccessary
    if i % 2 == 0:
        print(list_fr[i])


