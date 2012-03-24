# http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python/6581949#6581949


# Dynamically creating a class
SomeClass = type('MyShinyClass', (), {})
print SomeClass

some_instance = SomeClass()
print some_instance
print some_instance