def print_me(arg):
  print arg

# Integers pass by value
def modify_int(i):
    i = i + 1
    print i

# Floats pass by value
def modify_float(f):
    f = f + 1.1
    print f

# Lists pass by reference
def modify_list(l):
    l.append(1)
    print l


print_me("Hello")

i = 3
print i
modify_int(i)
print i

f = 3.1
print f
modify_float(f)
print f


l = [1,2,3]
print l
modify_list(l)
print l