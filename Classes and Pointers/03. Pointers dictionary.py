# In this program we will see pointers with respect to dictionary

dict1 = {
    'value': 11
}

dict2 = dict1

print("Before value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)
print("\ndict1 points to: ", id(dict1))
print("\ndict2 points to: ", id(dict2))

dict2['value'] = 22
#After redeclaring the key value of dict2
print("After value is updated:")
print("dict1 = ", dict1)
print("dict2 = ", dict2)
print("\ndict1 points to: ", id(dict1))
print("\ndict2 points to: ", id(dict2))

'''
Here unlike integers, when a variable which was pointing to a dictionary gets updated then it 
affects both the dictionaries, hence both 'dict1' and 'dict2' have the same address after value
is updated.
'''


