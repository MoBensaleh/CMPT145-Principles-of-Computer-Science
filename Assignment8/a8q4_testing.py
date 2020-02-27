# Mohamed Bensaleh
# CMPT 145 Assignment 8
# 11254030
# Mob127

import a8q4 as a8q4
import treenode as node
import treebuilding as tb


#### Testing path_to method
test_cases = [
    {'args_in': [None, None], 'expected': (False, None), 'reason': 'Empty tree'},
    {'args_in': [(node.create(1, node.create(1))), 1], 'expected': (True, [1]), 'reason': 'Tree with one repeated node'},
    {'args_in': [(node.create(1, node.create(2), node.create(3))), 3],
     'expected': (True, [3, 1]), 'reason': 'Tree with multiple nodes and value'},
    {'args_in': [(node.create(1, node.create(2), node.create(3))), 4],
     'expected': (False, None), 'reason': 'Tree with multiple nodes and no value'},
    {'args_in': [(node.create(1, node.create(2), node.create(3, node.create(4), node.create(5)))),
                 2], 'expected': (True, [2,1]),
     'reason': 'Tree with many nodes and value'},
    {'args_in': [(node.create(1, node.create(1))), 0],
     'expected': (False, None), 'reason': 'Tree with one node and no value'},
]

for test in test_cases:
    args = test['args_in']
    expected = test['expected']
    result = a8q4.path_to(args[0], args[1])

    if result != expected:
        print('Test failed: path_to(): got "' + str(result) \
              + '" expected "' + str(expected) + '" -- ' + test['reason'])

#### Testing find_path method
test_cases = [
    {'args_in': [None, None, None], 'expected': None, 'reason': 'Empty tree'},
    {'args_in': [(node.create(1, node.create(1))), 1, 0], 'expected': None, 'reason': 'Tree with one repeated node and 1 value in the path'},
    {'args_in': [(node.create(1, node.create(2), node.create(3))), 1, 3],
     'expected': [1, 3], 'reason': 'Tree with multiple nodes and 2 values'},
    {'args_in': [(node.create(1, node.create(2), node.create(3))), 1, 2],
     'expected': [1, 2], 'reason': 'Tree with multiple nodes and 2 values at front'},
    {'args_in': [(node.create(1, node.create(2), node.create(3, node.create(4), node.create(5)))),
                 2, 5], 'expected': [2, 1, 3, 5],
     'reason': 'Tree with many nodes and 2 values'},
    {'args_in': [(node.create(1, node.create(1))), 0, 19],
     'expected': None, 'reason': 'Tree with one node and no value'},
    

]

for test in test_cases:
    args = test['args_in']
    expected = test['expected']
    result = a8q4.find_path(args[0], args[1], args[2])

    if result != expected:
        print('Test failed: find_path(): got "' + str(result) \
              + '" expected "' + str(expected) + '" -- ' + test['reason'])

# more tests for find_path
print(a8q4.find_path(node.create(1, node.create(2), node.create(3, node.create(4), node.create(5))), 5, 1))
print(a8q4.find_path(node.create(1, node.create(2), node.create(3, node.create(4), node.create(5))), 5, 2))
print(a8q4.find_path(node.create(1, node.create(2), node.create(3)), 4, 1))

print('***Testing Complete***')