def main():
    number = get_number()
    print(f"Fibonacci Number {number}:", fib(number))    

def get_number():
    while(True):
        n = int(input("Number: "))
        if n > 0: 
            return n
    
def fib(m):
    x,y,f = 0,1,0
    for _ in range(m-1):
        f = x + y
        y = x
        x = f
    return x

if __name__ == '__main__':
    main()