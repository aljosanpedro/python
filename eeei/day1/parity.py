def main():
    number = get_number()
    print(parity(number))

def get_number():
    while(True):
        n = int(input("Number: "))
        if n > 0:
            return n

def parity(n):
    return n%2

if __name__ == '__main__':
    main()