def addition(list):
    ans=0
    for i in list:
        ans+=i
    print("Sum ",ans)
def maxoflist(list):
    ans=list[0]
    for i in list:
        if ans<i:
            ans=i
    print("Max ",ans)
def main():
    list=[]
    n=int(input("Enter number to be in the list : "))
    for i in range(0,n):
        list.append(int(input(f"Enter numbers : {i} ")))
    addition(list)
    maxoflist(list)
if __name__=="__main__":
    main()