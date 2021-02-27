def comprehensions():
    x_values = [2*value for value in range(5)]
    x_values_two = [value + 0.8 for value in x_values]
    return x_values, x_values_two

value, two = comprehensions()

print(value)
print(two)

my_array = ["Vikram", "Peter", "Michael", "Cuthbert", "Anita"]

another_array = [word[0] == "V" for word in my_array]




