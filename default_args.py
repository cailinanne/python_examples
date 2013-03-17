
def print_array(foo, args=['banana', 'apple', 'fruit']):
    if 'a' in foo:
        args.remove('apple')

    print "%s" % args


print_array("b")
print_array("c")
print_array("a")
print_array("d")


