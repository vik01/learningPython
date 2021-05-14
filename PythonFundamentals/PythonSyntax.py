# Commenting a line is done by using '#'
# This program goes over python basics

# To print to console, use the print() command
# Inside the brackets is a String which is a block 
# of text that is readable to humans. You can show 
# a string is two ways; single/double quotes.
print("Hello World")

# Variables
# store a specific data type and can be reused later
# variables also take space in memory (not a lot tho)
# Since this variable is a String type variable, you can 
# add it to the print() call.
meal = "An english muffin"
print(meal)

# Errors, two initial types
# SyntaxError: something wrong with the way the 
#              program is written. Eg, missing 
#              parenthesis or wrong punctuation
print("Change the last double quote to a single and you'll get a red line")

# NameError: occurs when Python sees something 
#            that is does not recognize. Eg, 
#            wrongly spelled variable.
print(mea)

# Numbers
# Integer (int): a whole number recognized by Python.
#                Contains positive/negative numbers.
#                but not decimal numbers.
value = 2

# Float point: numbers with decimals 
floatingNumber = 9.38329

# Calculations through +, -, *, /
# when dividing, Python 3 converts all int types
# to float types for better precision.
# calculations follow mathematical order
# of operations

# prints "574"
print(573 + 1)

# prints 5.0
print(10 / value)

# special error called ZeroDivisionError
print(10 / 0)

# prints 8 because '**' means to the 
# power of. Therefore this expression 
# can be seen are 2^3.
print(2 ** 3)

# Modulo is the remainder after division
# in the case below, when you divide 11 by
# 10, the remainder is 1. Hence prints 1.
print(11 % 10)

# Concatenation is adding strings together.
# Use the '+' operator to add two strings.
# However, it puts it together without an 
# space inbetween. So add a space between to 
# make the sentence readable.
# prints "An english muffin, Yummy!"
print(meal + ", yummy!")

# adds the left value to the current right value 
value += 4

# Multi-line Strings
# use three quote-marks to show multi-line strings
greetings = """Hello, how are you
                hope today went great!""" 






