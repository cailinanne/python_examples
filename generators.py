# Create a list, iterate around it (twice)
print "list"
my_list = [1, 2, 3]
for i in my_list :
    print(i)

for i in my_list :
    print(i)

# Create a list using a list comprehension, iterate around it (twice)
print "list comprehension"
my_list = [x*x for x in range(1,5)]

for i in my_list :
    print(i)

for i in my_list :
    print(i)

print "list comprehension with filter"
my_list = [x*x for x in range(1,5) if x % 2 == 0]

for i in my_list :
    print(i)

# Now use a generator
# The iteration only works once because with generators the values are not stored in memory
# just used then discarded
print "generator"
my_generator = (x*x for x in range(4))
for i in my_generator :
    print(i)

for i in my_generator :
    print(i)