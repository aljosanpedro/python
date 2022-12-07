def main():
    dividend,divisor,quotient,remainder = 0,0,0,0

    dividend = int(input("Dividend: "))
    divisor = int(input("Divisor: "))

    answers = qnr(dividend,divisor)
    quotient,remainder = answers[0],answers[1]
    
    print("Quotient:", quotient)
    print("Remainder:", remainder)

def qnr(n,m):
    return [round(n/m,2), n%m]

if __name__ == '__main__':
    main()