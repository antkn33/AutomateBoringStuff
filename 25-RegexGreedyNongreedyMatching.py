# 154-157

import re

# ? means to find if it exists 0 or 1 times
batRegex = re.compile(r"Bat (wo) ?man") # finds "wo"
mo = batRegex.search("The adventures of Batman") # mo is match object
mo.group()
# returns "Batman" because wo appers 0 times

mo = batRegex.search("The adventures of Batwoman")
mo.group()
# "Batwoman" - wo appears 1 time

mo = batRegex.search("The adventures of Batwowowowoman")
mo == None # True - returns None. wo appers many times

# phone number search
phoneNumRegex = re.compile(r"\(\d\d\d\)-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("My number is (616)-450-1603")
mo.group()
# Returns "(616)-450-1603"

# ? after area code means its optional. can appear 0 or 1 times
phoneNumRegex = re.compile(r"(\d\d\d\)?\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("My number is 450-1603")
mo.group()
# Returns "450-1603"

# * star character. Can appear 0 or more times
batRegex = re.compile(r"Bat (wo)*man") # finds "wo" 0 or more times
mo = batRegex.search("The adventures of Batwowowowman") # mo is match object
mo.group()
# returns "Batwowowowman"

# + match one or more
batRegex = re.compile(r"Bat (wo)+man") # finds "wo" 1 or more times
mo = batRegex.search("The adventures of Batman") # mo is match object
mo.group()
# returns None

# find a specifc number of times (3)
batRegex = re.compile(r"Bat (wo)(3)man") # finds "wo" 0 or more times
mo = batRegex.search("The adventures of Batwowowowman") # mo is match object
mo.group()
# returns "Batwowowowman"
# can use (3,5) to match a range of 3-5
# or (,5) means 0-5

digitRegex = re.compile(r"(\d)(3,5)")
digitRegex.search("1234567890")
# returns "12345" because it does 'greedy' matche first.
# goes for the largest amount

digitRegex = re.compile(r"(\d)(3,5)?") # ? does a non-greedy match
digitRegex.search("1234567890")
# returns "123" a non-greedy match

