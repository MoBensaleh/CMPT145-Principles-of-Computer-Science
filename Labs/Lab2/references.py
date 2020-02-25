# CMPT 145



print('Example: Copying References')
x = [1, 2, 3]
y = x
print('before', x, y)
y[0] = 100
print('after ', x, y)


print('Example: Copying Lists')
x = [1, 2, 3]
y = x[:]  # copies the list
print('before', x, y)
y[0] = 100
print('after ', x, y)



print("Example: List expressions")
x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print('before', x, y, z)
x[0] = 100
y[0] = 999
print('after ', x, y, z)



print('Example: multi-dimensional lists')

x = [[0, 1, 2], [5, 6, 7]]
y = [[10, 11, 12], [15, 16, 17]]
z = x + y
print('before', x, y, z)
x[0][0] = 999    # change first element of first sublist
y[0][0] = 100    # change first element of first sublist
print('after ', x, y, z)



print('Example: list products')

x = [1, 2, 3] * 3
print('before', x)
x[0] = 10
print('after ', x)



print('Example: list products copy references')

x = [[0, 1, 2]] * 3
print('before', x)
x[0][0] = 10
print('after ', x)


print('Example: functions and parameters')

def change_params(a):
    a = a - 1
    return a

a = 5
b = 10
print('before', a, b)
b = change_params(a)
print('after ', a, b)


print('Example: functions and and immutable arguments')

def swap_ints(x, y):
    print('inside swap_ints(), before', x, y)
    tmp = x
    x = y
    y = tmp
    print('inside swap_ints(), after ', x, y)

a = 3
b = 4
print('global scope, before', a, b)
swap_ints(a, b)
print('global scope, after', a, b)


print('Example: functions and and mutable arguments')

def swap_in_list(a_list, i, j):
    tmp = a_list[1]
    a_list[1] = a_list[2]
    a_list[2] = tmp

some_list = ['a', 'list', 'of', 'words']
print('before', some_list)
swap_in_list(some_list, 1, 2)
print('after ', some_list)

