# menu_card = ['Panner','Biriyani','Rice']
# print('Available Items in menu card : ',menu_card)

# menu_card.append('Idly')
# print('After using append method : ',menu_card)

# #Extend method ---> Add the elements of a list (or iterable)
# #to the end of the list
# menu_card.extend(['Dal','Dosa'])
# print('After using extend method : ',menu_card)

# #Insert - will add according to the position
# menu_card.insert(1,'VegBiriyani')
# print('After using insert method : ',menu_card)

# #Remove() method -> will remove specified value
# menu_card.remove('Idly') 
# print('After using remove method : ',menu_card)

# #Pop() method ->removes on position wise
# menu_card.pop(2)
# print('Using pop method : ',menu_card)

menu_card = ['Panner','Biriyani','Dosa','Panner']
#Index method

Index_method = menu_card.index('Dosa')
print('It will give the position : ',Index_method)

Index_method = menu_card.index('Panner')
print('It will give the position : ',Index_method)

#sort method
menu_card.sort()
print('Using Sort method : ',menu_card)
































































































