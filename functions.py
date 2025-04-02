#
# builtin function
# import first
import random
random.randint(1, 10)

# import sys, os, math

# terminate program early
import sys
sys.exit

# third party

# install with pip
import pyperclip
pyperclip.paste
pyperclip.copy

# writing your won functions
def hello():
    print('howdy')
    print('Hello')
    print('Hola')
hello()
hello()
hello()

#
def hello(name): # naem is parameter
    print('Howdy ' + name)
hello('Anthony') # Anthony is an arguement

#
def plusOne(number):
    return number + 1
newNumber = plusOne(5)
print(newNumber) # returns 6

# print return a none value

# keyword arguements
# print has end and sep keyword arguements

# Local and Global Scopes



