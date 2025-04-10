#
import re

message = "Call me at 616-450-1603. Or try 616-648-0994 for my office"

# r is a raw string. /d represents a numeric digit
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# mo is variable name for match object. search is the method for searching
# search methond only finds 1st occorence.
# use findall() to return all occurences
#mo = phoneNumRegex.search(message)
print(phoneNumRegex.findall(message))

# group is the method for returning the search
# don't need this if using findall()
# print(mo.group())
