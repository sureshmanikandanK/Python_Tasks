def add(num01, num02):
    return num01 + num02

def sub(num01, num02):
    return num01 - num02

def mul(num01, num02):
    return num01 * num02

def div(num01, num02):
    if num02 == 0:
        return "Error: Division by zero is not allowed."
    return num01 / num02

def main():
    operations = {
        1: ('Addition', add),
        2: ('Subtraction', sub),
        3: ('Multiplication', mul),
        4: ('Division', div)
    }
    
    print('Choose operation:')
    for key, (name, _) in operations.items():
        print(f'{key}. {name}')
    
    select = int(input('Select 1/2/3/4: '))
    
    num01 = int(input('Enter 1st number: '))
    num02 = int(input('Enter 2nd number: '))

    if select in operations:
        operation_name, operation_function = operations[select]
        result = operation_function(num01, num02)
        print(f'{operation_name} of {num01} and {num02}: {result}')
    else:
        print("Invalid selection. Please try again.")

if __name__ == '__main__':
    main()
