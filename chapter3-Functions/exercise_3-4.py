#! /usr/bin/python

# 1. Type this example into a script and test it. 
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)
print('')

# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument. 
def print_spam(s):
    print(s)

def do_twice(f, arg):
    f(arg)
    f(arg)

do_twice(print_spam, 'testy mcgee')
print('')

# 3. Write a more generalized version of print_spam, called print_twice, that takes a string as a parameter and prints twice. 
def print_twice(arg):
    print(arg)
    print(arg)

print_twice('testy mcthree')
print('')

# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.\
def do_twice(f, arg):
    f(arg)
    f(arg)

do_twice(print_twice, 'spam')

print('')

# 5.  Define a new function called do_four that takes a function object and a value and calls the
#     function four times, passing the value as a parameter. There should be only two statements in
#     the body of this function, not four.

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'tricky')