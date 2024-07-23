watch_details = {
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000
}

#Keys()-> returns a list containing the dictionarys keys
key_method = watch_details.keys()
print('Key Method:',key_method)

value_method = watch_details.values()
print('Value Method:',value_method)

#get method -> returns the value of a specified key
get_method = watch_details.get('Titan')
print('Get Method:',get_method)


#items() method
item_method=watch_details.items()
print('Item Method:',item_method)

#update({}) method->insert an item inot the dictionary
watch_details.update({'Noise':12000})
print('Updated Method:',watch_details)

#pop() method ->Remove element with the specified key
watch_details.pop('Titan')
print('Poped Method:',watch_details)
#Creating a set 
staff_id={123,124,125,126}#same data type
mixed_type ={'Moni',25,124,True,124}#mixed data type
print('Set:',mixed_type)
print('Length:',len(mixed_type))

s1 = {True,0,1,False}
print(s1)


s1={True,1}
print(s1)

#task -> iterate using for loop
# mixed_type ={'Moni',25,124,True,124}


# for mixed in mixed_type:
#     print(mixed)
mixed_type ={'Moni',25,True,124}
more_add={'Ravi',23}
# add() method -> add element to the set
mixed_type.add('Hello')
print(mixed_type)

# update() method
mixed_type.update(more_add)
print(mixed_type)

# discard() method -> remove Specifi element
mixed_type.discard(True)
print(mixed_type)

# remove() method
mixed_type.remove('Hello')
print(mixed_type)