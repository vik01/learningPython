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

    # methods with the "self" parameter are able to use the fields in 
    # the class. However you do not need to call that parameter
    # when you call the function
    def create_fraction(self):
        return str(self.numerator) + " / " + str(self.denominator)


# A class must be instantiated (created an instance of) 
# in order for the class to perform what it is meant to do.
fraction = Fraction(10, 20)

# class variables: data of that class
num = fraction.numerator
den = fraction.denominator

# call function that has self parameter
complete_fraction = fraction.create_fraction()
# will be "10 / 20"
print(complete_fraction)

# uses the __repr__ dunder method
print(fraction)

