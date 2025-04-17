# handling bugs and errors
 # raise - rasises and exception message

raise Exception('This is an error message')  # your own message

# Example - prints a box
# Exceptions should generally be used for user errors

"""
****************
*              *
*              *
*              *
*              *
****************
 
"""
import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1')
    if (width < 2) or (heigth < 2):
        raise Exception('"width" and "heigth" need to be 2 or greater')
    
    print (symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print (symbol * width)


# try:
# except: 
#     errorFile: open('error_log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('Traceback was written to error_log.txt')

# will raise the symbol length exception
boxPrint('=!', 5, 20)

# Error:
"""
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
Cell In[1], line 13
     10     print (symbol * width)
     12 # will raise the symbol length exception
---> 13 boxPrint('=!', 5, 20)

Cell In[1], line 3, in boxPrint(symbol, width, height)
      1 def boxPrint(symbol, width, height):
      2     if len(symbol) != 1:
----> 3         raise Exception('"Symbol" needs to be a string of length 1')
      4     if (width < 2) or (heigth < 2):
      5         raise Exception('"width" and "heigth" need to be 2 or greater')

Exception: "Symbol" needs to be a string of length 1

 """


##################
# assertions - another kind of exception
# used for programmer errors

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

switchLights(market_2nd)

# Bug is that lights could be green and yellow. One must be red. 
# so you should add an assert statement to check for a rec light

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(intersection)

switchLights(market_2nd)

