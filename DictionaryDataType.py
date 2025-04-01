#
myCat = {'size': 'large',
         'color': 'black',
         'disposition': 'loud',}
        # key is size
        # value is large
myCat['size'] # large

# dictionaries are unordered
# order doesn't matter for comparison
# no 'first' item

# tryin to access a non existent key 
# for a key gives a key error
#myCat['height'] # keyerror: 'height'

# check for a key
'size' in myCat
True

# like lists, they hold a reference
# methods
list(myCat.keys())
size color dispostion

list(myCat.vlaues())
large black loud

list(myCat.items())
#    returns [('size', 'large'),
#          ('color', 'black'),
#          ('disposition', 'loud')]

myCat = {'size': 'large',
         'color': 'black',
         'disposition': 'loud',}
for k, v in myCat.items():
    print(k, v)

# get method
myCat.get('height', 0) # is the fallback if color doen't exist
# result is 0

# setdefault method
# sets a value to a defualt if it doesn't exist
myCat.setDefault('size', 'small')
# wont change if value exists

import pprint # pretty print
message = 'Ask the user if they want to get another card.'
count = {}

for character in message.upper():
    count.setdefault(character, 0) # sets count to 0 to begin with
                                    # 
    count[character] = count[character] + 1
pprint.pprint(count)
# or
# formatText = pprint.pformat(count)
# print(formatText)


