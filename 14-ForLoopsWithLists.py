# For loops with list, multiple assignments, augmented operators

list(range(4))
    # [0,1,,2,3]

list(range(0, 100, 2))
    # 0 -98, by 2's

supplies = ['pens', 'staplers', 'flame throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

''''
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame throwers
Index 3 in supplies is: binders
'''

# multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
# size will be 'fat'
# color will be 'orange'
# disposition will be 'loud'

# augmented operators
spam = 0
spam += 1
# also have -= , *= , /=, %=




