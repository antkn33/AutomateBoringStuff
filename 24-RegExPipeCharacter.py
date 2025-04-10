import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

mo = phoneNumRegex.search("My number is 616-450-1603")
mo.group()
# returns "616-450-1603"

# divide the regex into groups with ()
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo.group(1)
# returns "616"
mo.group(2)
# returns "450-1603"

# if phone number contains (). place a \ right before the ()
phoneNumRegex = re.compile(r"\(\d\d\d\)-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("My number is (616)-450-1603")
mo.group()
# Returns "(616)-450-1603"

# pipe character | 
# find "Bat" with all the listed suffixes
import re
batRegex = re.compile(r'Bat(man|mobile|copter|woman)')
# mo = batRegex.findall("Batman married Batwoman and left in Batmobile")
# mo.group()
print(batRegex.findall("Batman married Batwoman and left in Batmobile"))
