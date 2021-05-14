# Classes are created using the 'class' word
class Fraction:
    # dunder methods (__init__ is like constructors)
    # have double underline 
    # __init__() is a constructor which is executed when 
    # the class is initialized
    def __init__(self, num, den):
        if (den == 0):
            return "Denomintor cannot be zero" 

        self.numerator = num
        self.denominator = den

        # Also add a instance variable in this conctructor
        self.double_value = num / den

    # A dunder method which is a string representation of the class
    # is called whenever you just print out the class object
    def __repr__(self):
        return "Fraction is: " + str(self.numerator) + " / " + str(self.denominator)

    # Second dundar method which returns true if the numerator is present in the fraction
    # is called when you instentiate the contains(fraction object) method.
    def __contains__(self, numerator):
        return self.numerator == numerator

    # methods with the "self" parameter are able to use the fields in 
    # the class. However you do not need to call that parameter
    # when you call the function
    def get_fraction(self):
        return str(self.numerator) + " / " + str(self.denominator)


# A class must be instantiated (created an instance of) 
# in order for the class to perform what it is meant to do.
fraction = Fraction(10, 20)

# class variables: data of that class
num = fraction.numerator
den = fraction.denominator

# call function that has self parameter
complete_fraction = fraction.get_fraction()
# will be "10 / 20"
# print(complete_fraction)

# uses the __repr__ dunder method
# print(fraction)

# Inheritance is when a class inherits the data and methods of another classes
# The inheritor is the subclass or child class, while the base class is called the parent classes
class FractionInteger(Fraction):
    pass


# Overriding methods
# You can overide a parent classes methods by calling the same method in the child classes
# In the below example, the user needs to check the username before changing the message.
# However, the Admin (Inherits from User) can just add the message. They are the same methods.
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
  
class Admin(User):

  def edit_message(self, message, new_text):
    message.text = new_text

# Super: makes a call from the child class method to the parent class method
# super() gives us a proxy object. With this proxy object, 
# we can invoke the method of an object’s parent class (also called its superclass)
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):

  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40

# Interfacing
# When two classes have the same method names and attributes, we say they implement the same interface. 
# An interface in Python usually refers to the names of the methods and the arguments they take.
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

# same interface as HomeInsurance
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return (0.001 * self.price_of_insured_item)

# same interface as VehicleInsurance
class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return 0.00005 * self.price_of_insured_item

# Polymorphism: the idea that the addition of muliple same arguements will result in an intuitive sum of same arguments. 
# The '+' operator does many things depending on context, int + int = int, list + list = list, etc.
# Polymorphism is an abstract concept that covers a lot of ground, 
# but defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code.
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"
# the len method introduces polymorphism where it can take any argument and return the sum of its indexes.
print(len(a_list))
print(len(a_dict))
print(len(a_string))


# Example taken from CodeCademy

# Dundar Methods allow for polymorphism, by allowing use to add a dundar method named __add__ which 
# acts like the + operator. 

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        """Dundar method __str__ invoked when you call pring on an user-defined object (e.g. Color)
        """
        return f"Color of RGB: red -> {self.red}, green -> {self.green}, blue -> {self.blue}"

    def __add__(self, other):
        """Dundar method __add_ invoked when you use the + operator to add multiple user-defined objects (e.g. Color)
        """
        new_red = min(self.red + other.red, 255)
        new_green = min(self.green + other.green, 255)
        new_blue = min(self.blue + other.blue, 255)

        return Color(new_red, new_green, new_blue)

red = Color(255, 0, 0)
blue = Color(0, 0, 255)

magenta = red + blue

print(magenta)

# Putting it all together
class SortedList(list):
  def __init__(self, lst):
    super().__init__(lst)
    return super().sort()

  def append(self, value):
    super().append(value)
    super().sort()
  
  def __len__(self):
    return super().__len__()


test = SortedList([3, 5, 1, 4, 2])
test.append(-3)
test.append(-5)
print(test)
print(len(test))

for number in test.iter():
  print(number)

