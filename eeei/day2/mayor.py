def main():
    command,money,done = '',0,False

    while(not done):
        command = prompt(money)
        effects = turn(command,money,done)
        money,done = effects[0],effects[1]

def prompt(n):
    print("Money:", n)
    
    while(True):
        x = input("Command: ")
        if len(x) == 1:
            return x

def turn(c,m,d):
    match c:
        case '+': m += 100
        case '-': m -= 100
        case 'o': pass
        case '*': m *= 2
        case '/': m //= 2
        case 'x': 
            print("Game Over!")
            print("Score:", m)
            d = True
        case  _ : m -= 20

    return [m,d]

if __name__ == '__main__':
    main()