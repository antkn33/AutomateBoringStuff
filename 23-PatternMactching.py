#
# Pattern Matching
def isPhoneNumber(text):
    if len(text) != 12:
        return False # not correct length for phone number
    for i in range(0, 3): # 1st 3 numbers
        if not text[i].isdecimal():
            return False # Not area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no 1st 2 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # no last 4 digits
    return True

# print(isPhoneNumber('6164501603'))

# Detect phone number in  a string

message = "Call me at 616-450-1603. Or try 616-648-0994 for my office"
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12] # goes through each character & checks a
                            # 12 character chunk
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
        foundNumber = True
if not foundNumber:
    print("Could not find a valid phone number.")

