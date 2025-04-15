# ch 8 
# Paths
# 'c:\\Users\\anthony' # Must have \\ to escape the \
# or use raw strings
# r'c:\Users\Anthony'

import os

# joins strings in to a path for whichever OS is being used
path = os.path.join('Users', 'anthonyscott', 'Downloads') 
print(path)

os.getcwd() 
#   gets current working directory
os.chdir() 
#   takes string to change directory

# absolute path c:\users\anthony
# relative - to current working directory
    # \Documents\VSCode = c:\users\anthony\Documents\VSCode
# . = this directory
# .. = parent directory

os.path.abspath(spam.png)
# returns  c:\users\anthony\Documents\VSCode\spam.png

os.path.isabs() # is it an absolute path True or False

os.path.relpath('c:\\users\\anthony\\Documents\\VSCode', 'c:\\users')
# returns: '../c:\\users\\anthony\\Documents\\VSCode'

os.path.dirname  # path name
os.path.basename  # after the final slash - filename

os.path.exists(r'/Users/anthonyscott') # returns True ( or False)

os.path.isfile
os.path.isdir

os.path.getsize('path to file')
os.listdir('path of folder')


# List files and sizes in  folder
import os

folder = os.getcwd()
totalSize = 0

for filename in os.listdir(folder):
    if not os.path.isfile(os.path.join(folder, filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(folder, filename))
print(totalSize)

# os.makedirs
