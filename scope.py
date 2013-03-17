
# If else clauses do not have scope
if 1==1:
    s = "hello"
else:
    s = "boo"


print s


# try/except do not have scope
try:
    u = "blah"
except Exception:
    pass

print u