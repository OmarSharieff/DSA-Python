# Let us consider

num1 = 11
num2 = num1

#Before updating num2
print("Before num2 value is updated:")
print("num1 = ",num1)
print("num2 = ",num2)
print("\nnum1 points to: ", id(num1))
print("\nnum2 points to: ", id(num2))

#After updating num2 value
num2 = 22
print("After num2 value is updated:")
print("num1 = ",num1)
print("num2 = ",num2)
print("\nnum1 points to: ", id(num1))
print("\nnum2 points to: ", id(num2))

'''
If you run this code, the output of 'num2' id before updating will be same as the 'num1' id. 
But after redeclaring 'num2' to 22, the id of 'num2' changes and now "num1' and 'num2' have 
different ids. 
'''