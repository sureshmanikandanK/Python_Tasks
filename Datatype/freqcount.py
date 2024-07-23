def count_num(list, number):
    count = 0
    for i in list:
        if i == number:
            count += 1
    return count

def main():
    print('Enter the size:')
    size = int(input())
    data_input = []

    print('Enter the values:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User List:', data_input)
    
    search_num = int(input('Enter the element to check if it is repeated: '))
    print(search_num, 'is repeated', count_num(data_input, search_num), 'times')

if __name__ == "__main__":
    main()
