# Functions: blocks of code which are run when 
#            the function is called
# Code in the function will be indented with 
# while spaces. 
def hello_world(iy):
    print("Hello World!")

hello_world(iy = 1)

# Multiple Returns 
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit, target

low, high, hello = get_boundaries(100, 20)

print("All values: " + str(low) + " " + str(high) + " " + str(hello))

# Python Code Challenges: Functions

# Function takes a value and returns the
# value to the 10th power
def tenth_power(num):
    return num ** 10

# Function takes a value and returns
# the square root of the value
def square_root(num):
    return num ** 0.5

# Function takes two values, win and lose
# returns the percentage of wins
def win_percentage(wins, loses):
    result = wins + loses
    return 100 * (wins / result)

# Function takes two vales and returns
# the average.
def average(num1, num2):
    result = num1 + num2
    return result / 2

# Function takes two values and returns
# the remainder of the expression
def remainder(num1, num2):
    return (2 * num1) % (0.5 * num2)

# Advanced Python Code Challenges: Functions

# Function takes a value and prints out
# three of the values multiples. Returns
# the last one
def first_three_multiples(num):
    print("The first multiple is " + str(num))
    print("The second multiple is " + str(num * 2))
    print("The third multiple is " + str(num * 3))
    return num * 3

# Function takes a total payment and 
# tip percentage and returns the amount
# that should be paid to the waiter
def tip(total, percentage):
    return (percentage / 100) * total

# Function takes in first and last name
# and returns name James Bond Style
def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

# Function takes in name and age
# and returns a string of the age in dog years
def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"

# Function does miscellaneous math stuff
def lots_of_math(a, b, c, d):
    print(str(a + b))
    print(str(c - d))
    print(str((a + b) * (c - d)))
    return ((a + b) * (c - d)) % a

# Calculates the estimated American Insurance cost of a person based on their
# age, sex, bmi, number of children, and if they are a smoker
# returns the estimated insurance cost.
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = "The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars."
  return estimated_cost, output_message

def calculated_difference(num1, num2):
    result = num1 - num2
    print("The difference in insurance cost is " + result + " dollars")