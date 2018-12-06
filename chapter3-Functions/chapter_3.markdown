# Chapter 1 - Functions
https://www.greenteapress.com/thinkpython/thinkpython.pdf


## 3.1 Function Calls
1. A __function__ is a named sequence of statements that performs a computation. You specify the name and the sequence of statements. Then you later call the function by its name. 
2. The _parenthesis_ of a function is called the __argument__ of the function. 
3. The _result_ of a function is a __return value__. 

## 3.2 Type conversion functions
1. Python has built in functions that convert a value from one type to another. 
    * _int_
    * _float_
    * _string_ 

2. _int_ converts a number to an integer, and chops off hte end of a float. _float_ converts strings and integers to a floating point. _string_ converts int and floats to a string. 

## 3.3 Math functions 
1. Python has a __math module__. This module contains a collection of related functions. 
```python 
import math
```
2. You can access modules in math using __dot notation__ 
```python
raio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
```

## 3.4 Composition
1. you can combine all the previous lessons learned (varialbes, expressions, and statements)
2. The left side of an assignment statement has to be a variable name. 

## 3.5 Adding new functions
1. A __function definition__ specifies a function name and the sequence of statements that execute when its called. 
2. You can't use a keyword as the name of a function. 
3. Empty parenthesis after a function name indicate that a function does not take parameters. 
4. The first line in hte function definition is called the __header__. The rest is called the __body__. 
5. Single quotes and double quotes do the same thing. Single quotes are most often used. 
6. If you type a function defintion in interactive mode, the interpreter prints (...) to let you know that the definition is not complete. 
```python 
pyth>>> def print_lyrics():
... print "I'm a lumberjack, and I'm okay."
... print "I sleep all night and I work all day."
```

## 3.6 Definitions and uses
1. __function defintions__ are executed like nay other statement, but they also create function objects. 
```python 
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()
```
    * there are two function definitions above, _print_lyrics_ and _repeat_lyrics_
2. You have to create a a function before executing it. 

## 3.6 Ezxercises
1. Exercise 3.1 - The script has a "NameError: name 'repeat_lyrics' is not defined". It seems as though an undefined function is a name error. 
2. Exercise 3.2 - The script created a "NameError: global name 'print_lyrics' is not defined". It seems as though there is a global namespace error. 


## 3.7 Flow of execution
1. To know if a function is defined, you have to know the __flow of execution__.
2. Execution starts at the first statement in a program. Statements are executed one at a time from top to bottom. 
3. Function Definitions do not alter the flow of execution. Statements inside a function are not executed until the function is called. 
4. Its often better to not read a program from top to bottom, but from the _flow of execution_. 

## 3.8 Parameters and arguments
1. Functions can require arguments. 
2. You can define arguments as parameters. 
3. You can name your parameters anything you want. When calling that function, what you pass in to the function gets named the parameter during runtime. 

## 3.9 Variables and parameters are local
1. When you create a variable inside a function it is __local__. This _local_ variable only exists inside the function. 
2. You can get a NameError when trying to reference a local variable outside the scope of the function. 

## 3.10 Stack Diagrams
1. Keep track of where variables are used using a __stack diagram__. Stack diagrams show the value of each variable and they show the function each variable belongs to. 
2. Each function is represented by a __frame__. The name of the function is on the outside of the frame and the variables are inside the frame. 
3. When you create a varaible outside of any function, it belongs to _ _main_ _ _cannot bold main()_.
4. If an error occurs during a function call, then Python prints tha name of the function, and the name of the function that called that all the way back to main(). This list of functions is called the __traceback__. 
    * what file
    * what line
    * what functions

## 3.11 Fruitful functions and void function 
1. __fruitful functions__ return a value. __Void functions__ perform an action, but don't return a value. 

## 3.12 Why functions?
1. Creating functions allows you to groups statements, which makes it easier to debug. 
2. Make programs smaller by eliminating repetitive code. 
3. Create larger programs from smaller sections (_functions_)
4. Well designed functions are useful for many programs. 

## 3.13 Import with from
1. import with import
```python
import math
```
2. import with from
```python
from math import pi
```
## 3.14 Debugging
1. save issues inherent with tabs by only using spaces. 
2. Save your program before you run it. 
3. Make sure that the code that you are looking at is the code that is running. 

## 3.16 Exercises
1. Figuring out the solution to the column seventy took a moment. I realized that column seventy meant seventy spaces from the left. It took me a moment to realize that I could use math an the string " " to get the length. It was fun little problem. See the attached file. 
2. 







