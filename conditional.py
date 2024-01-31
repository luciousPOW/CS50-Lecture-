

# User input
x = int(input('x: '))
y = int(input('y: '))

# Good design
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is equal to y')

# Other method of if else
x = int(input('x: '))
y = int(input('y: '))
# Bad
if x < y or x > y:
    print('x is not equal to y')
else: 
    print('x is equal to y')
    
# Perfect method 
x = int(input('x: '))
y = int(input('y: '))
if x != y:
    print('x is not equal to y')
else:
    print('x is equal to y')


"""

# User input
x = int(input('x: '))
y = int(input('y: '))

# Good design
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
elif x == y:
    print('x is equal to y')
"""

"""
# User input
x = int(input("What's x? "))
y = int(input("What's y? "))

# Poorly logically design
if x < y:
    print('x is less than y')
if x > y:
    print('x is greater than y')
if x == y:
    print('x is equal to y')
    """