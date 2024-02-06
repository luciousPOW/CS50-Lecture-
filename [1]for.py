while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    
for _ in range(n):
    print('Meow')



# print('Meow\n' * 3, end="")

"""
# Good 
for _ in range(3): # we can use _ variable if that's not important 
    print('Meow')
"""
"""
# bad
for i in [0,1,2]:
    print('Meow')
"""
