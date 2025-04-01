#
# Strings
##########

list('Hello')
# returns
['H', 'e', 'l', 'l', 'o']

name = 'Anthony'
name[0] # returns A
name[1:3] # returns nt
name[-2] # returns n
'ony' in name # resturns True

# string values are immutable. 
# the value can't be changed
# lists are mutable. The values can be changes

# modify a string
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
# Zophia the cat

# assigning a list to a variable is a refernce 
# to the list. If it is changed, it is changed 
# everywhere

# lists can be changed and accessed outside of a function
# creates a totally separate copy of a list
import copy
spam = ['hello', 'hi', 'howdy', 'heyas']
cheese = copy.deepcopy(spam) # seperate from spam

# line continuation
spam = ['hello', 
        'hi', 
        'howdy', 
        'heyas']
# \
print("Four score" + \
       "and seven")
