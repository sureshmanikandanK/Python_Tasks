# Watch_details={
#     'Titan':856650,
#     'Fatrack':50000,
#     'Omega':90000,
#     'Titan':12222
# }

# #len() #type()

# print(len(Watch_details))
# print(type(Watch_details))
# print(Watch_details['Titan'])
# print(Watch_details)

# Watch_details={
#     'Titan':5000,
#     'Fatrack':50000,
#     'Omega':90000,
#     'Sonata':5000
# }
# print(len(Watch_details))
# print(type(Watch_details))
# print(Watch_details['Titan'])
# print(Watch_details)

# Watch_details['Rolex']=40000
# print(Watch_details)

# #Create 
# Food_items={
#     'Dosa':50,
#     'Idly':5,
#     'Chapathi':20,
#     'Vada':5
# }
# print(Food_items)
# print(len(Food_items))
# print(type(Food_items))
# print(Food_items['Dosa'])
# print(Food_items)

#Nested Dictionary

users = {
   'suresh':{
        'firstname': 'suresh',
        'lastname': 'manikandan',
        'location': 'chennai'
    },
   'sathish':{
        'firstname': 'sathya',
        'lastname': 'narayanan',
        'location': 'bangalore'
    },
   'deva':{
        'firstname': 'vaishnu',
        'lastname': 'deva',
        'location': 'mumbai'
    },
}

print(users)         
print(len(users))     
print(type(users))    
print()

for std in users.items():
    print(f"User ID: {std}")
