# class student:
#     @staticmethod
#     def Rollnumber(y):
#         print('Inside Static Method :',y)

# student.Rollnumber(101)

# s1=student()
# s1.Rollnumber(102)

class student:
    @staticmethod
    def Rollnumber(y):
        print('Inside Static Method :',y)

student.Rollnumber=staticmethod(student.Rollnumber())
student.Rollnumber(101)