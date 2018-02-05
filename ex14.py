# this one is like your scripts with argv

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)

# ok, that *args is pointless. we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)
	
# this takes just one argument
def print_one(arg1):
	print "arg1: %r" %arg1
	
# this won't take any arguments
def print_none():
	print "i got nothing."
	
# invoking the functions
print_one("first one")
print_two("sai", "kamat")
print_two_again("sai", "kamat")
print_none()