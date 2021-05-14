#Key value pairs
# {key: value, key: value...}
my_dictionary = {"Vikram": 19, "Pinto": 20, "Jasmine": 22}

# Add key-value pairs to dictionary
my_dictionary["Mac"] = 20

# Add multiple key-value pairs
my_dictionary.update({"lucia": 20, "Marco": 23, "Itachi": 33})

# Overwrite is the same as adding to a existing key
my_dictionary["Mac"] = 19

# List comprehension to dictionariesm0nnnnnnnnnnnnnnnnnnnnnnnnnn
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)


# Selecting from a dictionary
# Prints 19
print(my_dictionary["Vikram"])

#Use .get and specify a return type (second value) if the thing is false
print(my_dictionary.get("Vikram", 100))

# check if key exists
value = "Norbit"
if value in my_dictionary:
    print("Yes")

try:
    print("Yes")
except KeyError:
    print("unknown person in my dictionary")

# Delete a Key, can specify a return value
my_dictionary.pop("lucia", 'Character DNE')

# get all keys of the dictionary
for key in my_dictionary.keys():
    print(key)

# Get all values of a dictionary
for value in my_dictionary.values():
    print(value)

# For all items (key and value)
for value, value2 in drinks_to_caffeine.items():
    print(value + " and " + value2)
