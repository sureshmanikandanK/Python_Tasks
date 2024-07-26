# def sum_all(*args):
#     count=0
#     for i in args:
#         count += i
#     return count

# output = sum_all(1,2,3,4,5)
# print('addition:',output)

# def main(*args):
#     name=""
#     for i in args:
#         name = i
#     return name

# std=main(['suresh','Ravi','Ajith','Sala'])
# #std=['suresh','Ravi','Ajith','Sala']

# if __name__=="__main__":
#     main(['suresh', 'Ravi', 'Ajith', 'Sala'])
#     print(std)

# def main(*args):
#     if len(args) == 0 or not isinstance(args[0], list):
#         raise ValueError("No list argument provided")
    
#     lst = args[0]
#     if len(lst) == 0:
#         raise ValueError("List is empty")
    
#     name = ""
#     for item in lst:
#         name += item + " "  # Concatenate each item followed by a space

#     name = name.strip()  # Remove the trailing space
#     return name

# std = main(['suresh', 'Ravi', 'Ajith', 'Sala'])
# print(std)  # Output: suresh Ravi Ajith Sala

# if __name__ == "__main__":
#     std = main(['suresh', 'Ravi', 'Ajith', 'Sala'])
#     print(std)  # Output: suresh Ravi Ajith Sala


# def main(*args):
#     for j in args:
#         for i in j:
#             print(i)

# if __name__=="__main__":
#     main(['suresh', 'Ravi', 'Ajith', 'Sala'])


def StaffDetails(**kwarg):
    for key,value in kwarg.items():
        print(f'{key} is {value}')
# StaffDetails(Name='Suresh',
#                   Age=21,
#                   MobileNum=1123445)
def main():
    changepond = {'Name':'Suresh',
                  'Age':21,
                  'MobileNum':1123445}
    StaffDetails(**changepond)
if __name__ == "__main__":
    main()