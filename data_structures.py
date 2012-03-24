import logging
logging.basicConfig(level=logging.DEBUG,format="%(message)s")

# TUPLES
t = ()
logging.info("The length of my empty tuple is: %d", len(t))
logging.info ("The empty tuple is: %s", t)

t = (1,)
logging.info ("Tuple with one entry: %s", t)

# "Pack" the letters a, b, c into the tuple
t = ('a','b','c')
logging.info (t)
logging.info (t[1])

try:
    t[0] = 'd'
except TypeError:
    logging.info ("Tuples are immutable")

# "Unpack" the values of the tuple
x, y, z = t
logging.info(x)

# SETS
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
logging.info(fruit)

# LISTS
l = [1,2,3]
l.append(4)
logging.info(l)
logging.info(l.pop())
logging.info(l)

for v in l:
    print v

for index, value in enumerate(l):
    print index, value

# LIST COMPREHENSIONS

squares = [x**2 for x in range(10)]
logging.info(squares)

# DICTIONARIES

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.iteritems():
    print k, v
