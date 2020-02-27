# test script sample
# replace inputs, expected output, and reason for each test case with the data you want to test


##########################
# len function unit test #
##########################

test_cases = [
    {'inputs'  : [1, 2, 3],
     'outputs' : 3,
     'reason'  : 'Check length of a list with positive numbers'},

    {'inputs'  : [-1, 2],
     'outputs' : 2,
     'reason'  : 'Check length of a list with negative numbers'},

    {'inputs'  : [2, "cat"],
     'outputs' : 2,
     'reason'  : 'Check length of a list with different data type elements'}
]


for t in test_cases:
    l = t['inputs']
    expected = t['outputs']

    # replace the len function with the function you want to test. Usually, you will need to import your aXqY file first.
    result = len(l)
    if result != expected:
        print('Error in check(): expected ', expected[0],
              ' but got ', result, '--', t['reason'])



#############################################
# len and remove functions integration test #
#############################################

test_cases = [
    {'inputs'  : [[1, 2, 3], 1],
     'outputs' : 2,
     'reason'  : 'Check length of a list after removing a positive number'},

    {'inputs'  : [[-1, 2], -1],
     'outputs' : 1,
     'reason'  : 'Check length of a list after removing a negative number'},

    {'inputs'  : [[2, "cat"], "cat"],
     'outputs' : 1,
     'reason'  : 'Check length of a list after removing a string'}
]


for t in test_cases:
    l = t['inputs'][0]
    element_to_remove = t['inputs'][1]
    expected = t['outputs']
    # in the integration test you have at least two functions working together to check the final result. Here the function remove is being called
    # before the len function.
    l.remove(element_to_remove)

    # replace the len function with the function you want to test. Usually, you will need to import your aXqY file first.
    result = len(l)
    if result != expected:
        print('Error in check(): expected ', expected[0],
              ' but got ', result, '--', t['reason'])
