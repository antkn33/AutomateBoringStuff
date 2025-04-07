#
# dictionary of cat attributes
import pprint

allCats =[] # list for all cats

# add dictionaries of cat attribues
allCats.append({'name': 'Tommy',
        'size': 'large',
         'color': 'black',
         'disposition': 'loud',})
allCats.append({'name': 'Jerry', 
        'size': 'small',
         'color': 'orange',
         'disposition': 'quiet',})

# PrettyPrint
pprint.pp(allCats)
allCats[1]
# type function
# type(42) # int
# type(allCats) # list