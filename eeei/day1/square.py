def main():
    side = get_side()
    print("Area:", area(side))

def get_side():
    while(True):
        x = int(input("Side: "))
        if x > 0:
            return x

def area(n):
    return pow(n,2)
    
if __name__ == '__main__':
    main()