# 157-159

import re

phoneNumRegex = re.compile(r"\d\d\d\-\d\d\d-\d\d\d\d")

text = "My home number is 450-1603, work number is 616-648-0994, cell number is 616-648-5396"

phoneNumRegex.findall(text)
# returns a list ['616-648-0994', '616-648-5396']

"""
\d any numeric digit 0-9
\D anything NOT a numeric digit 0-9
\w any letter, numeric digit or underscore. 
\W anything NOT a letter, numeric digit or underscore. 
\s any space. tab or newline character
\S anything NOT a space. tab or newline character

"""
import re

lyrics = "1 Partridge in a pear tree, 2 turtledoves, 3 French hens, 4 calling birds, 5 golden rings, 6 geese a-laying, 7 swans a-swimming, 8 maids a-milking."

xmasRegex = re.compile(r"\d+\s\w+") 
# match a digit - \d, a space - \s, followed by one or more words \W+1
xmasRegex.findall(lyrics)

# creating our own classes. []
vowelRegex = re.compile(r"[aeiouAEIOU]") # same as "a|e|i|o|u..."
vowelRegex = re.compile(r"[aeiouAEIOU]{2}") # finds two conescutive vowels
vowelRegex = re.compile(r"[^aeiouAEIOU]") # finds everything except vowels. includes spaces, etc

                        
