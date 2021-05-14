# A lambda function is a one line function which runs basic operations (sort of like boolean zen)
# You can also use an 'if' statement for a lambda function in the form: <return if true> if <check> else <return if false>
is_string = lambda my_string: my_string in "This is my master string"


# True
print(is_string("This"))
# False
print(is_string("Hola"))

# Example of if statment with lambda function is
is_orange = lambda fruit: 'is an orange' if fruit == 'orange' else 'is not an orange'
apple = is_orange('Apple')
orange = is_orange('orange')
print(f'Apple {apple}')
print(f'Orange {orange}')

