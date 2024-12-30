def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)

'''
As there are Two for loops 
No. of operations = n+n = 2n
So, here Big(O) is O(2n)
As we drop constants, it is O(n)
'''