#
import re

namesRegex = re.compile(r'Agent \w+')
namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
# output is ['Agent Alice', 'Agent Bob']


import re
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'REDACTED gave the secret documents to REDACTED.'

import re
namesRegex = re.compile(r'Agent (\w)\w*')
namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
# ['A', 'B']

import re
namesRegex = re.compile(r'Agent (\w)\w*')
namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.') # \1 is first group
# 'Agent A**** gave the secret documents to Agent B****.'

# Verbose, allows to use whitespace and comments
import re
re.compile(r'''
           (\d\d\d)|  # area code without parens
           (\(\d\d\d)) # -or- area code with parens
           -
           \d\d\d # prefix
           -
           \d\d\d\d # last 4 digits''', re.verbose) 

# compile function - | is OR operator
#, re.IGNORECASE | re.DOTALL | re.VERBOSE  
# will use all three compile functions





