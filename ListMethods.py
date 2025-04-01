#
# 
spam = ['hello', 'hi', 'howdy', 'heyas']
# .index() is a method
spam.index('hello') # retuen 0

spam.append('holla')
spam.insert(1, 'bye') # inserts at index 1

# don't use as a variable
# these are only used for lists

spam.remove('hi')
# remove specifies as a value
# whereas del removes at a position
del spam[0]

spam.sort()
spam.sort(reverse=True)
# All uppercase letters come before lowercase letters
# A B C a b c

# true alpabetical
spam.sort(key=str.lower)



