#Consider a program
n = 10
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

'''
Here n = 10, So the items printed are from '00' to '99 i.e, total of 100 operations done
therefore operations done in a nested for loop = O(n) * O(n)
Time Complexity of nested for loop = O(n^2) 
'''
