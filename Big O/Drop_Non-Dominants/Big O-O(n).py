def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_items(10)

'''
As there are one nested loop and one for loop
The no. of operations = n2 + n
As we drop non-dominants i.e n, the big O is O(n2)
'''