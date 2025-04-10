#
# returns a new string
spam = 'Hello World!'
spam.upper()
'HELLO WORLD!' # NEW STRING
spam
# still returns 'Hello World!'

# change the string
spam = spam.upper()
spam
# returns 'HELLO WORLD!' 

spam.lower()
# hello world!

spam.isupper()
# False if str is in lower case
spam.islower()

isalpha() # letters only
isalnum() # only letters and numbers
isdecimal() # numbers only
isspace() # whitespace only
istitle() # titlecase only

spam.startswith('H') # True
spam.endswith('p') # False

# Join
', '.join(['cats', 'bats', 'rats'])
# 'cats, bats, rats' - one string
'\n'.join(['cats', 'bats', 'rats'])
# cats
# bats
# rats

# Split
'My name is Anthony'.split()
# ['My', 'name', 'is', 'Anthony']

'My name is Anthony'.split('m')
# ['My na', 'e is Anthony']

'Hello'.rjust(10)
# '     Hello' - inserts spaces so total length is 10

'Hello'.rjust(10, '*')
 # '*****Hello'

'Hello'.ljust(25, '-')
# 'Hello--------------------'

'Hello'.center(25, '-')
# '----------Hello----------'

# Strip
spam = 'Hello'.rjust(10)
spam.strip() # removes whitespace

spam.lstrip()
spam.rstrip()
spam.strip ('o')
spam.replace('e', 'o') # 'Hollo'

# pyperclip module
import pyperclip
pyperclip.copy('heloooo') # can paste anywhere on computer
pyperclip.paste() # returns string 'heloooo'

# String Formatting
name = "Alice"
place = "my house" 
time = "6 pm"
food = "turnips"
"Hello %s, you are invited to a party at %s at %s. Please bring %s." % ("Alice", "my house", "6 pm", "turnips")
# or you can do - % (name, place, time, food)
