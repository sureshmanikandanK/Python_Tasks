def Userinput():
    marks = {}
    marks["Tamil"] = int(input("Enter the Tamil Mark:"))
    marks["French"] = int(input("Enter the French Mark:"))
    marks["Maths"] = int(input("Enter the Maths Mark:"))
    marks["Science"] = int(input("Enter the Science Mark:"))
    marks["Social"] = int(input("Enter the Social Mark:"))
    return marks
 
def Grades(marks,result):
    Total = sum(marks.values())
    if Total >= 400:
        return result[400]
    elif Total <=399 and Total >=300:
        return result[300]
    elif Total <=299 and Total >=200:
        return result[200]
    elif Total < 200:
        return result[100]
def main():
    result = {
        400:"Your Grade: O :)",
        300:'Your Grade: A',
        200:"Your Grade: B",
        100:'Your Grade: F'}
   
    marks = Userinput()
    print()
    print("****Result****")
    print(Grades(marks,result))
if __name__ == "__main__":
    main()