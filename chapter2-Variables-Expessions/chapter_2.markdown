# Chapter 2: Variables, expressions, and statements
https://www.greenteapress.com/thinkpython/thinkpython.pdf


## 2.1 Values and types
 1. __values__ are something a program works with. _ex. 1,2 , 'Hello'_
 2. __types__
    * _integer_
    * _string_
    * _float_
    * _etc_
3. find the type of an object with _type_
```python
type('Hello, World!')
type(4000)
```
## 2.2 Variables
1. You can assign variables
```python
message = 'everyone for themselves!!!!'
n = 17 
pi = 3.141592
```
2. You can use a state diagram to convey variable assignment on paper. 

## 2.3 Variable names and keywords
1. choose names that are meaningful. 
2. varibles have to begin with a number. 
3. It is better to start a variable with a lowercase letter. 
4. Invalid names will give you syntax errors. 
    * 18banannas --> starts with a number
    * frequenttrips@ --> has the @ symbol
    * class --> used by Python as keyword

## 2.4 Operators and operands
1. __Operators__ are symbols that represent computation like... + / - = 
2. __operands__ are vales acted on by the _operators_
3. '^' is known as XOR in Python
4. Python 2 has 31 protected keywords
    * and
    * as 
    * assert
    * break
    * class 
    * continue
    * def
    * del
    * elif
    * else
    * except
    * exec
    * finally
    * for 
    * from 
    * global
    * if 
    * import
    * in 
    * is
    * lambda
    * not 
    * or 
    * pass
    * print
    * raise
    * return 
    * try 
    * while
    * with 
    * yield 
5. In Python 3, the result of a division is a _float_. The new '//' operator performs floor division. 


## 2.5 Expressions and statements 
1. __expression__ is a combination of values, variables, and operators. 
2. a __statement__ is a unit of code that a Python interpreter can execute. 

## 2.6 Interactive mode and script mode
Interactive mode, such as being in the pyton command line intepretor is not the same as script mode. Using the command line interpreter calculator functions will not work the same when you run the same commands as a script. 

## 2.7 Order of operations
1. Order follows __rules of precedence__. 
2. Order of operations follows the acronym __PEMDAS__
    * _Parenthesis_
    * _Exponentiation_
    * _Multiplication and Division is greater than Addition and Subtraction
    * Operators with the same precendence moves left to right. 

## 2.8 String operations
1. You cannot perform math on strings, _ex. '2' - '1' 'eggs'/'easy' 
2. The '+' (plus sign) however performs concatenation. This is linking end-2-end. 

## 2.9 Comments
1. Long programs needs additional explanation in a natural language (__English__, Spanish, etc)
```python
# the '#' creates comments
inline_comment = 'the following is an inline comment'  # as you can see
```

## 2.10 Debugging
1. syntax errors have little additional info. 
2. runtime errors help track down items that have been misspelled. 
3. after syntax and runtime errors come semantic errors, which means that you need to track through your program to find out where the program differs from your expectations. 

## 2.12 Exercises
__Exercise 2.2__ 
Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'

For each of the following expressions, write the value of the expression and the type (of the value of
the expression).
1. width/
    * expected: 8.5
    * actual: 8.5
2. width/2.0
    * expected: 8.5
    * actual: 8.5
3. height/3
    * expected: 4.0
    * actual: 4.0
4. 1 + 2 * 5
    * expected: 11
    * actual: 11
5. delimiter * 5
    * expected: '.....'
    * actual: '.....'

__Exercise 2.3__
1. The volume of a sphere with radius r is 4/3πr^3. What is the volume of a sphere with radius 5?
Hint: 392.7 is wrong!
```python
>>> (4/3)* 3.14 * 5 ** 3
523.3333333333334
``` 

2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

```python
book = 24.95 
cost_per_book = book*(0.6)  # the store gets 40% discount, so they pay 60% per book
bookstore_book_cost = cost_per_book * 60 
shipping_cost = 3 + (.75 * 59)
wholesale_cost = bookstore_book_cost + shipping_cost
```

>>> wholesale_cost
945.4499999999999

3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?


```python
# converting seconds to minutes for standard additions
# start time 6:52, assume adding in minutes. 
hour_left = 6
leave_house_time = 52
jog_pace_initial = 8 + (15/60)
jog_pace_fast = 7 + (12/60)
pace_one_total = jog_pace_initial * 2
pace_two_total = jog_pace_fast * 3
total_time_jogging = pace_one_total + pace_two_total
total_time = leave_house_time + total_time_jogging
total_time = total_time / 60
time_return = hour_left + total_time
```










