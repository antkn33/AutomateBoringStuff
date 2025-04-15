# 197 -200

# Shell Utility
import shutil

# shutil.copy('file', '..')

# copy and rename
shutil.copy('hello.txt', '/Users/anthonyscott/bye.txt')

# copy all folder & contents
# rename to backup
shutil.copytree('Users/anthonytscott', 'Users/backup')

# move
shutil.move('file path', 'new file path')

# rename a file, but not move or copy
# or use a path string
shutil.move('hello.txt', ' bye.txt')

