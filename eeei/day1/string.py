def main():
    number = get_number()
    text = input("Text: ")
    print(repeat(number,text))

def get_number():
    while(True):
        x = int(input("Number: "))
        if x > 0:
            return x

def repeat(n,s):
    return n*s

if __name__ == '__main__':
    main()