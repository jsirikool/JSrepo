# Test .py file

name = raw_input("What's your name? ")
print "%s, nice to meet you!" % name

from sys import argv
script, arg1, arg2 = argv
print "Hello %s script, Here is %r and %r, have at it!" % (script, arg1, arg2)

