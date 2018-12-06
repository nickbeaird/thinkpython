#! /Users/nbeaird/.pyenv/shims/python

# Solution 1 
def horizontal():
    mid_line = ('- ' * 4)
    line = '+ ' + mid_line + '+ ' + mid_line + '+'
    print(line)
    
    empty_mid = (' ' * len(mid_line))
    space_line = ('| ' + empty_mid + '| ' + empty_mid + '|')
    print(space_line)
    print(space_line)
    print(space_line)
    print(space_line)
    print(line)
    print(space_line)
    print(space_line)
    print(space_line)
    print(space_line)
    print(line)

horizontal()


# Solution 2

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end=" ")

def print_post():
    print('|        ', end=" ")

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
