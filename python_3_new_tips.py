# f-string, to avoid string formatting
name='Sai'
age=30
print_output = f"hi this is {name} & I'm {age} years old"
print(print_output)

#help function
# help(print)

# find size of any object
# memory consumption directly attributed to the object 
import sys
x = [1, 2, 3, 4]
y = 'superman'
print(sys.getsizeof(x))
print(sys.getsizeof(y))

# Chaining of Comparison Operators
# to check more than two conditions
a = 5
if 2<a<6:
    print('pass')

# list comprehensions
# a more elegant way of making lists without filling them end to end

supers_list = "superman, batman, wonder woman, aquaman, flash, green lantern, hawk girl"
find_vowels = [i for i in supers_list if i in "aeiou"]
print(find_vowels)

# string multiplication
print("ho!"*3+"merry christmas!")

# assign multiple variables in single line
power_levels_goku, power_levels_gohan, power_levels_krillin = 1000000, 100000, 1000
print(power_levels_goku, 
power_levels_gohan, 
power_levels_krillin)

# swapping variables
# usually you swap variables in three lines, and have to use a temporary variable, like:
# temp = x;  x = y; y = temp;
# can be done in single line
A = 10
B = 20
print('before swap:')
print(A, B)
A, B = B, A
print('after swap:')
print(A, B)

# using enumerate
# enumerate is an automatic counter which assigns a index value pair to elements in a list

my_list = ['a', 'b', 'c']
for i, val in enumerate(my_list):
    print(i, val)


# dir()
# the dir() is a pretty powerful function and lists all the attributes, functions & methods
# that can be used for a particular variable. 
# it's primarily used for debugging purposes.
# print(dir(my_list))
print(my_list.__sizeof__())
print(sys.getsizeof(my_list))

# unpacking splat operator
# used to unpack function arguments such that they can be used individually for various 
# purposes.


def foo(*args):
    print(args)

foo(2, 3)
foo('a', 'b', 'c', 'd')
