import os

def delete_file(filename):
    if not os.path.exists(filename):
        print(f'File not exists: {filename}')
    else:
        os.remove(filename)
        print(f'{filename} has been deleted')

def main():
    file_to_delete = input('Enter the name of the file to delete: ')
    delete_file(file_to_delete)

if __name__ == "__main__":
    main()
