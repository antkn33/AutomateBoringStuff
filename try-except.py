def div42by(divideBy):
    try:
        return 42 / divideBy
    
    except ZeroDivisionError: # error for dividing by zero
    # except: will catch all errors
        print("Error: you tried to divide by zero")

print(div42by(2))
print(div42by(12))
print(div42by(0)) # will print the error above
print(div42by(1))

