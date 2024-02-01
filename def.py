def main():
    number = get_number()
    meow(number)
    
def meow(n):
    for _ in range(n):
        print('meow')
        
def get_number():
    while True:
        n = int(input('Enter number: '))
        if n > 0:
            break
    return n
        
        
main()