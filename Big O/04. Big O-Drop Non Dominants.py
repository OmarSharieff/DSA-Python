#Consider a program
n = 10
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

'''
Here we have a nested for loop and a normal for loop. We know that the time complexity for nested loops
are O(n^2) and time complexity for a normal loop is O(n). Therefore the time complexity for the 
function print_items is O(n^2) + O(n) = O(n^2+n). But 'n' here is very insignificant compared to 
n^2 when we have large values for n like in thousands or millions. As the number becomes larger
the standalone n is a very small portion of the number of operations. So we don't consider O(n)
and drop it as it is a non-dominant.
Therefore the time complexity = O(n^2)
'''