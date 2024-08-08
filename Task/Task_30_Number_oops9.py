# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.


from functools import reduce
class Number:

    def __init__(self) :
        self.value = float(input("Enter Number : "))

    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value /2) + 1):
            if self.value % i == 0:
                return False
        return True

    def ChkPerfect(self):
       
        return self.SumFactors() == int(self.value)
    
    def SumFactors(self):
        sumfactor = self.Factors()
        return sum(sumfactor)

    def Factors(self):
        factors=[]
        for i in range(2, int(self.value)+1):
            if int(self.value)%i==0:
                factors.append(i)

        return factors

num = Number()
if (num.ChkPrime()):
    print(f'{num.value} is a Prime Number')
else:
    print(f'{num.value} is not a Prime Number')

if (num.ChkPerfect()):
    print(f'{num.value} is a Perfect Number')
else:
    print(f'{num.value} is not a Perfect Number')

print(num.Factors())

print(num.SumFactors())