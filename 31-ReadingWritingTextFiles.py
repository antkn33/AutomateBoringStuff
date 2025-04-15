# 181-185
# Plain text files
helloFile = open('hello.txt') # or a path
helloFile.read()
helloFile.close()

helloFile.readlines() # list of strings

# write 
helloFile = open('hello.txt', 'w')
# append
helloFile = open('hello.txt', 'a')

helloFile = open('hello2.txt', 'w')
helloFile.write('Hello!!!!!')
helloFile.close

# Shelf file dictionary, lists, 
import shelve
shelfFile = shelve.open('mydata')
shelfFile['dogs'] = ['Sassy', 'Yeti', 'Oli']
# ['Sassy', 'Yeti', 'Oli']

list(shelfFile.keys())
# ['dogs']

list(shelfFile.values())
# [['Sassy', 'Yeti', 'Oli']]
shelfFile.close()





