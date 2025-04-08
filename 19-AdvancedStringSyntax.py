# 
# escape character
print("Say hi to Bob\'s mother") # single quote escape


"""

\" double quote
\t Tab
\n new line
\\ backslash

"""

# raw string
print(r'That is Carol\'s cat')
# That is Carol\'s cat

# Multi line strings
print(""" This
      is 
      a
      multi
      line
      string""")


# treating a string like a list
spam = 'Hello World!'
spam[0] # 'H'
spam[1:5] # 'ello'
spam[-1] # '!'
'Hello' in spam # True
'HELLO' in spam # False
