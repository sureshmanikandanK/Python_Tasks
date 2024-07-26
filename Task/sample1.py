#open() function -> filename, mode(r,w,a...)

# file_read = open('c:\Python\Task\Task\Task_3_calc.py','r')
# print(file_read.read())

import os
def CreateFile(filename):
    # filename = file_read.py
    if(os.path.exists(filename)):
        print('File alreay exists')
    else:
        file_create = open(filename,'w')

def main():
    print('Enter filename you want to create: ')
    file_name = input()

    CreateFile(file_name)

if __name__=="__main__":
    main()


#Hi this is sample text#Hi this is sample text2#Hi this sample text3