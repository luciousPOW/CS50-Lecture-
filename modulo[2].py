def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):
    # Turning the 4 lines of code below (multi-comment if else) into 1 line 
    return True if n % 2 == 0 else False
    
    """
    if n % 2 == 0:
        return True
    else:
        return False
    """
    
main()    




"""

x = int(input("What's x? "))

if x % 2 == 0:
    print('Even')
else:
    print('Odd')"""
