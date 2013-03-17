import logging
logging.basicConfig(level=logging.DEBUG,format="%(message)s")

# FILTER

# Show numbers that are not divisible by 2 or 3
l = range(2,25)
def f(x): return x % 2 != 0 and x % 3 != 0
l2 = filter(f,l)
logging.info(l2)
logging.info(l)

# FILTER WITH LAMBDA

l = range(2,25)
l2 = filter(lambda x: x %2 != 0 and x %3 != 0, l)
logging.info(l2)

# MAP

l = range(1,11)
def cube(x): return x*x*x
l2 = map(cube, l)
logging.info(l2)
logging.info(l)


# REDUCE
l = range(1,5)
def add(sum,x): return sum+x
sum = reduce(add, l, 0)
logging.info(l)
logging.info(sum)

# REDUCE WITH LAMBDA
sum = reduce(lambda a, b: a+b, l, 0)
logging.info(l)
logging.info(sum)


