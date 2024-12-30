def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)

'''
As it is a nested for loop 
No. of operations = n * n = n2
so, Big O is O(n2)
'''