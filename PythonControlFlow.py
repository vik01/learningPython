# Python if-elif-else statements

def ifStatements():
    count = 1
    if (count == 1):
        print("Number is 1")
    elif (count == 2):
        print("Number is 2")
    else:
        print("Number greater than 2")

# Try and Except Statements 
# Code in try statement executes 
# If a error is caused and the error 
# matches the one mentioned in the except statement, 
# the except statement will be executed.
def division(a, b):
    try:
        result = a / b
        print(str(result))
    except ZeroDivisionError:
        print("Cannot divide by zero")


# Python Code Challenges
def large_power(base, exponent):
    result = base ** exponent
    if (result > 5000):
        return True
    return False

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    cost = electricity_bill + internet_bill + food_bill + rent
    return cost > budget

def twice_as_large(num1, num2):
    return num1 > 2 * num2

def divisible_by_ten(num):
    return num % 10 == 0

def not_sum_to_ten(num1, num2):
    return num1 + num2 != 10

# Advanced Code Challenges
def in_range(num, lower, upper):
    return (num >= lower) and (num <= upper)

def same_name(my_name, your_name):
    return my_name == your_name

def always_false(num):
    if (num < 0):
        return False
    elif (num == 0):
        return False
    else:
        return False

def movie_review(rating):
    if (rating <= 5):
        print("Avoid at all costs!")
    elif (rating > 5 and rating < 9):
        print("This one was fun.")
    else:
        print("Outstanding!")

def max_num(num1, num2, num3):
    max = num1
    if (num2 > max):
        max = num2

    if (num3 > max):
        max = num3
    
    if ((num1 == num2) and max != num3):
        return "It's a tie!"
    elif((num1 == num3) and max != num2):
        return "It's a tie!"
    elif((num2 == num3) and max != num1):
        return "It's a tie!"
    
    return max
