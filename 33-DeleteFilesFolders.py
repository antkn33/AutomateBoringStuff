# 230-232

import os

# delete a file
os.unlink('file')

# delete folder
os.rmdir('folder path')
# folder must be empty

# delete folder and all contents
# !! permanent deletion
import shutil
shutil.rmtree('folder path')

# send2trash
# pip install send2trash

import send2trash
send2trash.send2trash('file string')


