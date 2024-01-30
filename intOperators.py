"""
# Function
def hello(to='World'):   
    print(f"Hello,", to)
  
# Hello World will be the default output if user call the function without arguments since 'World' is assigned to to.
hello() 

# User input
name = input('Enter name: ')    
hello(name) 
"""
# def main():
#     name = input("What's your name? ")
#     hello(name)
    
# def hello(to):
#     print(f"Hello,",to)
    
# main()

"""
# Calculator
def add(x,y):
    return x + y

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

print(add(num1,num2))
"""

def main():
    x = int(input('Enter x: '))
    print('x squared is:',square(x))
    
def square(n):
    # return n * n
    return pow(n, 2) # Second method of finding a square of user input

main()
