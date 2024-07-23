def frequency(str,letter):
    count=0
    for i in str:
        if(i==letter):
            count+=1
    return count

def main():
    string=input('enter the string: ')
    letter=input('enter the letter repeatation count: ')
    count=frequency(string,letter)
    print(count)

if __name__=="__main__":
    main()