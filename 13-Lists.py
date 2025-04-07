#

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0] # cat

spam = [['cat', 'bat'], [10,20,30]]
spam[0] # cat, bat
spam[0][1] # bat
spam[1][2] # 30

spam = ['cat', 'bat', 'rat', 'elephant']
spam = [-1] # elephant

# slices
spam[1:3] # bat, rat. Goes up to but not including
            # the third position. returns a NEW list

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'dog' # replaces bat with dog
spam[1:3] = ['roach', 'dog', 'mouse', 'fish']
    # ['cat', 'roach', 'dog', 'mouse', 'fish']

spam = ['cat', 'bat', 'rat', 'elephant']
spam[:2] # cat, bat
spam[1:] # bat, rat, elephant

# delete
del spam[2] # deletes rat

# number of items in a list
len([1,2,3]) # returns 3 
[1,2,3] + [4,5,6] # [1,2,3,4,5,6]
[1,2,3] * 3 # [1,2,3,1,2,3,1,2,3]

# list funtion
list('Hello') # ['H', 'e', 'l'. 'l', 'o']

'cat' in ['cat', 'bat', 'rat', 'elephant']
    # True
'cat' not in ['cat', 'bat', 'rat', 'elephant']
    # False





