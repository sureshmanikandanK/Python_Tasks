import os

def copy_file(file1, file2):
    if not os.path.exists(file1):
        print(f'File not exists: {file1}')
    else:
        file_1 = open(file1, 'r')
        Friends = file_1.read()
        
        file_2 = open(file2, 'w')
        file_2.write(Friends)
        print(f'Success -> Content copied from {file1} to {file2}')

def main():
    file1 = input('Enter the name of the file1: ')
    file2 = input('Enter the name of the file2 to be created: ')
    copy_file(file1, file2)

if __name__ == "__main__":
    main()