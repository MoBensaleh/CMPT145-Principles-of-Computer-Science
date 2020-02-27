# Mohamed Bensaleh
# Cmpt 145 Assignment 8
# 11254030
# Mob127


import a8q3 as a8q3
import treenode as node
import treebuilding as TB


#### Testing complete() method
test_cases = [
    {'args_in': [node.create(0,TB.build_complete(0))], 'expected': (True, 1), 'reason': 'small complete tree'},
    {'args_in': [node.create(0, TB.build_fibtree(9))], 'expected': (False, None), 'reason': 'Large incomplete tree'},
    {'args_in': [node.create(0,TB.build_complete(1))],
     'expected': (False, None), 'reason': 'small incomplete and uneven tree'},
    {'args_in': [node.create(0, TB.build_fibtree(2))],
     'expected': (False, None), 'reason': 'small incomplete tree'},
    {'args_in': [node.create(0, TB.build_fibtree(0))],
     'expected': (False, None),
     'reason': 'incomplete tree'},
    {'args_in': [node.create(1, node.create(2), node.create(3)), node.create(1, node.create(3), node.create(2))],
     'expected': (True, 2), 'reason': 'small complete tree'},
    {'args_in': [node.create(1, node.create(2))],
     'expected': (False, None), 'reason': 'small incomplete tree'},

]

for test in test_cases:
    args = test['args_in']
    expected = test['expected']
    result = a8q3.complete(args[0])

    if result != expected:
        print('Test failed: cmplt(): got "' + str(result) \
              + '" expected "' + str(expected) + '" -- ' + test['reason'])

print('***Testing Complete***')