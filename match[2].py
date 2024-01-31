name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print('Mcdo')
    case "Draco":
        print('KFC')
    case _:
        print('Who?')

"""
# Using match
name = input("What's your name? ")

match name:
    case "Harry":
        print('Mcdo')
    case "Hermoine":
        print('Mcdo')
    case "Ron":
        print('Mcdo')
    case "Draco":
        print('KFC')
    case _:
        print('Who?')

"""


"""
# Using if, elif and else
name = input("What's your name? ")

if name == "Harry" or name == "Hermoine" or name == "Ron":
    print('Mcdo')
elif name == 'Draco':
    print('KFC')
else:
    print('Who? ')
    """
