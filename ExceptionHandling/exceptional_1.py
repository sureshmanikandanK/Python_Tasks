# student_id = [101,102,103,104]
# try:
#     for i in range():
#         print(i,'-',student_id[i])
# except:
#     print('Index out of range')
import datetime
today = datetime.date.today()
year = today.year
print(year)
try:
    # num1=int(input("enter the num 1: "))
    # num2=int(input("enter the num 2: "))

    # result = num1/num2
    # print(result)

    items = ["Bread","Butter","Jam","Cheese"]
    # items[len(items)]="Spread"
    num1=int(input("enter the num 1: "))
    assert num1%2==0

except ZeroDivisionError:
    print("Error:Denominator cannot be zero")
except ValueError:
    print("Enter only numbers")
except IndexError:
    print("Kindly give the Proper index")
except AssertionError:
    print("Entered value does not meet the condition")
else:
    print(num1,"Is Even")
finally:
    print("Program is Over")

yob = int(input("Enter your year of birth"))

age = year - yob

if(age<18):
    raise Exception(f'The age should be 18 and your age is {age}')
print(age)#Suresh#Suresh