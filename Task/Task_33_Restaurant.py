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
    def __init__(self):
        self.restaurant_name = input('Enter the restaruant name : ')
        self.cuisine_type = input('Enter the restaruant cuisine type : ')

    def describe_restaurant(self):
        print(f' The restaurant name is {self.restaurant_name} and the cuisine type is {self.cuisine_type} ')
    def open_restaurant(self):
        print(f'The restaurant {self.restaurant_name} is open now')
    
restaurant1 = Restaurant()
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant()
restaurant2.describe_restaurant()
restaurant3 = Restaurant()
restaurant3.describe_restaurant()
restaurant4 = Restaurant()
restaurant4.describe_restaurant() 

