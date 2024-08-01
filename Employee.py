import datetime
today = datetime.date.today()
year = today.year

class Company:
    area = "Siruseri"
    __city = "Chennai"
    def __init__(self,cname):
        self._cname = cname
    def displaycname(self):
        print("Company Name: ",self._cname)
    def address(self):
        return self.area +" " + self.__city+ " TamilNadu";

class Employee:
    empcount=0
    isMarried = False

    def __init__(self,cname,fname,lname,yob):
        self._cname=cname
        self._firstname=fname
        self._lastname=lname
        self.__age=year-yob
        Employee.empcount +=1
        self.__empid=self.empcount

    def getempdetails(self):
        print("EmployeeId : ",self.__empid)
        print("Fullname: ",self._firstname,"",self._lastname)
        print("Age: ",self.__age)
        print("Marital Status: ",self.isMarried)


c1 = Company("Changepond Technologies")
c1.displaycname()
c1._city="Pune"
print("Address:",c1.address())

e1=Employee("Chennai","Suresh","Manikandan",2000)
e1.isMarried = True
e1.getempdetails();
e1=Employee("Mumbai","Ramesh","Kumar",2005)
e1.getempdetails();
e1=Employee("Pune","Rajesh","Kanna",1995)
e1.isMarried = True
e1.getempdetails();



# price
# Name
# description
