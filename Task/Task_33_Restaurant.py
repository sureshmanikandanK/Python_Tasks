# 9-1. Restaurant: Make a class called Restaurant. The init() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.
# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class Restaurant:
    def __init__(self,restaurant_name,cusine_type,):
        self.restaurant_name=restaurant_name
        self.cusine_type=cusine_type
        self.isopen=True
    def describe_restaurant(self):
        print(f' The restaurant name is {self.restaurant_name} and the cuisine type is {self.cusine_type} ')
    def open_restaurant(self):
        if self.isopen == 'open':
            print(f'The restaurant {self.restaurant_name} is open now')
        else:
            print(f'The restaurant {self.restaurant_name} is Close now')
class SalemRRR(Restaurant):
    def __init__(self, restaurant_name, cusine_type,isopen):
        super().__init__(restaurant_name, cusine_type)
        self.isopen=isopen
class Dhabha(Restaurant):
    def __init__(self, restaurant_name, cusine_type,isopen):
        super().__init__(restaurant_name, cusine_type)
        self.isopen=isopen
class KFC(Restaurant):
    def __init__(self, restaurant_name, cusine_type,isopen):
        super().__init__(restaurant_name, cusine_type)
        self.isopen=isopen

restaurant1 = Restaurant('fgdf','fdfudf')
rrr=SalemRRR("salem RRR hotel","south indian",False)
punjabi=Dhabha("Dhanbha","punjabi indian food",False)
kfc=KFC("KFC Chicken","Indian food",True)


restaurant1.describe_restaurant()
restaurant1.open_restaurant()

punjabi.describe_restaurant()
punjabi.open_restaurant()

kfc.describe_restaurant()
kfc.open_restaurant()

