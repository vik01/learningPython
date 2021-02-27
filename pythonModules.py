# modules are basically libraries which hold classes that we can use
# to do things. All module imports are at the top of the program.
from datetime import datetime
birthday = datetime(2001, 9, 9, 10, 30, 12)
current_time = datetime.now()
# String to interger date
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
# integer to string date
string_f_time = datetime.strftime(parsed_date, '%b %d, %Y')
print("birthday: " + str(birthday))
print("String converted to integer date: " + str(parsed_date))
print("Integer converted to string date: " + str(string_f_time))
print("Current time: " + str(current_time))


# Random
import random
# randint gets a random number between the two mentioned. 
random_list = [random.randint(1, 100) for i in range(1, 101)]
randomer_number = random.choice(random_list)
print(randomer_number)

# MatPlotLib
from matplotlib import pyplot as plt
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a, numbers_b)
plt.show()

# Decimal
from decimal import Decimal
single = Decimal('0.69')
double = Decimal('0.2')
two_decimal_points = single + double
print(two_decimal_points)
