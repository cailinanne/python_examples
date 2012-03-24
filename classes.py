# We'll put some classes here.
# Yup, we sure will!
import collections

def responds_to(instance, func):
    return isinstance(getattr(instance, func, None), collections.Callable)

class Cat():
    # This is a class variable or a "class attribute"
    num_legs = 4

    def __init__(self, name):
        # self.name is called a "data attribute"
        self.name = name



# There is no real concept of private member variables in Python
fred = Cat("fred")
print fred.name

joe = Cat("joe")
print joe.name

# Class variables can be accessed via the class or the object
print ""
print Cat.num_legs
print fred.num_legs
print joe.num_legs

# They cannot be modified via an instance though
# Trying to modify it via an instance actually creates a new
# data attribute on that particular object
joe.num_legs = 5
print ""
print Cat.num_legs
print fred.num_legs
print joe.num_legs

# They can be modified via the class
Cat.num_legs = 6
print ""
print Cat.num_legs
print fred.num_legs
# Since joe now has a data attribute with this name we
# wind up accessing that, and not the class attribute
print joe.num_legs

# Dynamically add a new method to a particular instance

def miaow():
    print "miaow!"

print ""
joe.miaow = miaow
joe.miaow()
print responds_to(joe,"miaow")
print responds_to(fred,"miaow")


# Dynamically add a new method to all instances
def scratch(self):
    print "scritch!"

Cat.scratch = scratch
joe.scratch()
fred.scratch()





