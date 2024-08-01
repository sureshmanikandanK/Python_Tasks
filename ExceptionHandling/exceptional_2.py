def file_using_handling(file_name):
    try:
        file_1 = open(file_name,'r+')
        file=file_1.read()
        print(file)
        # file_1.write("String")
        file_1.write("#Suresh")
        print(f'New content add to the file {file_1}')
    except FileNotFoundError as e:
        print(f'File not found check the given file name is correct or not {e}')

file_using_handling('c:\Python\Task\ExceptionHandling\exceptional_1.py')