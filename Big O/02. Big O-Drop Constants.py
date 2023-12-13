# Consider a program
n = 10
def print_items(n):
    #printing n items     
    for i in range(n):
        print(i)
    #printing n items
    for j in range(n):
        print(j)

'''
Now the time complexity of the print_items function appears to be O(n) + O(n) since there are
two for loops. O(n) + O(n) = O(2n). But we don't consider constant values and they are removed,
hence the time complexity is O(n)
'''