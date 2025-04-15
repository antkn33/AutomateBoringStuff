# 
import os

# os.walk() 
# returns 3 values

for folderName, subFolders, fileNames in os.walk('/Users/anthonyscott/Documents/VScode_Projects'):
    print(f"The folder is: {folderName}")
    print(f"The subfolders in {folderName} are: {str(subFolders)}")
    print(f"The files in {subFolders} are : {str(fileNames)}")
    print()
