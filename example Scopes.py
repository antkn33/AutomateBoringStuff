# local variables can't be accessed from outside the function
# either global variables or other local variables

spam = 42 # Global scope
def spam():
    eggs = 99 # Local scope. if there is an assignment in a function
               # ( = ), the variable is local. 
                # if not, ( print(eggs)) , it is global.
spam()
print(eggs) # NameError: name 'eggs' is not defined

# ==================

def spam():
    eggs = "Hello" # local variable
    print(eggs) # prints Hello

eggs = 42 # Global variable
spam()
print(eggs) # prints 42

# ======================


def spam():
    global eggs # defines eggs as a global variable
                # even if there is an assignment ( = )
    eggs = 99 
    
spam()
print(eggs)