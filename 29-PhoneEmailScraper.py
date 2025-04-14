# Reads copied text off of clipboard

import re, pyperclip

# Create a regex for phone numbers
# put the whole thing in a group so it returns a string per phone number


phoneRegex = re.compile(r'''
    (
    ((\d\d\d)|(\(\d\d\d\)))?                # area code
    (\s|-)                       # separator
    \d\d\d                           # first 3 digits
    -                         # separator
    \d\d\d\d                          # last 4 digits
    (((ext(\.)?\s)|x)
        (\d{2,5}))?    # extension
    )
    ''', re.VERBOSE)

# TODO : create a regex for email addresses
emailRegex = re.compile(r''' 
# name part 
    # character class
    [a-zA-z0-9_.+]+ # + st the end meansd match 1 or more   
# @ symbol
    @
# domain
    [a-zA-z0-9_.+]+
''', re.VERBOSE)
# get text off of clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0]) # [0] gets the first entry in the list of tuples

# print(allPhoneNumbers)
# print(extractedEmail)

# TODO : copy the extracted email/phone to the clipboard 
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)    # one phone number & email per line
print(results)
# pyperclip.copy(results) # copy results to clipboard
