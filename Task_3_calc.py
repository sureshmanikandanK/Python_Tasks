def Add(num01, num02):
    Ans = num01 + num02
    return Ans

def Sub(num01, num02):
    Ans = num01 - num02
    return Ans

def Mul(num01, num02):
    Ans = num01 * num02
    return Ans

def Div(num01, num02):
    if num02 == 0:
        return "Error: Division by zero is not allowed."
    Ans = num01 / num02
    return Ans

def main():
    print('Choose operation:')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    select = int(input('Select 1/2/3/4: '))
    
    
    num01 = int(input('Enter 1st number: '))
    num02 = int(input('Enter 2nd number: '))

    if select == 1:
        Ans = Add(num01, num02)
        print(f'Addition of {num01} and {num02}: {Ans}')
    elif select == 2:
        Ans = Sub(num01, num02)
        print(f'Subtraction of {num01} and {num02}: {Ans}')
    elif select == 3:
        Ans = Mul(num01, num02)
        print(f'Multiplication of {num01} and {num02}: {Ans}')
    elif select == 4:
        Ans = Div(num01, num02)
        print(f'Division of {num01} and {num02}: {Ans}')

if __name__ == '__main__':
    main()
