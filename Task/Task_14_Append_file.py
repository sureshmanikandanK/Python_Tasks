import os

def append(filename, Text):
    if not os.path.exists(filename):
        print()
        print(f'File not exists: {filename}')
    else:
        file_1 = open(filename, 'a')
        file_1.write(Text)
        print()
        print(f'Successful')

def main():
    file = input('Enter the name of the file to append: ')
    Text = input('Enter the content to append: ')
    append(file, Text)

if __name__ == "__main__":
    main()
