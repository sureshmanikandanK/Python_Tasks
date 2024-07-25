#using list comprehensive creating a list of sqare numbers
#new_list = [expression for member in iterable]
#new_list = [expression for member in iterable if (optional)]
 

new_list = [i for i in range(1,11)]
print('List Comperhension:',new_list)

new_list = [i for i in range(1,11) if(i%2==0)]
print('List Comperhension:',new_list)

