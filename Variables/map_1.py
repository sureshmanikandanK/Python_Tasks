from functools import reduce

def main():
    size = int(input('Enter the size:'))
    lst = []
    print('Enter Values:')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List:',lst) 
    course = ['',"Python","Java",";$",'angular']
    map_list = list(map( lambda num : num**3,lst))
    print('map List:',map_list)
    print()

    reduce_list = reduce((lambda num1,num2:num1+num2),map_list)
    print('Reduce value:',reduce_list)
    reduce_course = list(filter(lambda char:char!='a','q','z','s','w','x','d','e','c','v','f','r','t','g','b','h','y','n','j','u','m','k','i','l','o','p','Z','A','Q','W','S','X','C','D','E','R','F','V','B','G','T','Y','H','N','M','J','U','I','K','L','O','P'
),course)
    print('Reduce value:',reduce_course)

if __name__ == "__main__":
    main()


       