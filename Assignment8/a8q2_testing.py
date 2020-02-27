# Mohamed Bensaleh
# CMPT 145 Assignment 8
# 11254030
# Mob127

import a8q2 as a8q2
import treenode as node
import treetesting as tt


#### Testing mirrored method
test_cases = [
    {'args_in': [None, None], 'expected': True, 'reason': 'Empty tree'},
    {'args_in': [node.create(1), node.create(1)], 'expected': True, 'reason': 'Tree with one node'},
    {'args_in': [node.create(1, node.create(2), node.create(3)), node.create(1, node.create(3), node.create(2))],
     'expected': True, 'reason': 'Tree with multiple nodes1'},
    {'args_in': [node.create(1, node.create(2), node.create(3)), node.create(1, node.create(2), node.create(3))],
     'expected': False, 'reason': 'Tree with multiple nodes2'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(4), node.create(5))),
                 node.create(1, node.create(3, node.create(5), node.create(4)), node.create(2))], 'expected': True,
     'reason': 'Tree with multiple nodes2'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5))),
                 node.create(1, node.create(3, node.create(5), node.create(4, None, node.create(6))), node.create(2))],
     'expected': True, 'reason': 'Tree with multiple nodes3'},
]

for test in test_cases:
    args = test['args_in']
    expected = test['expected']
    result = a8q2.mirrored(args[0], args[1])

    if result != expected:
        print('Test failed: mirrored(): got "' + str(result) \
              + '" expected "' + str(expected) + '" -- ' + test['reason'])

#### Testing reflect method
test_cases = [
    {'args_in': None, 'expected': None, 'reason': 'Empty tree'},
    {'args_in': node.create(1), 'expected': node.create(1), 'reason': 'Tree with one node'},
    {'args_in': node.create(1, node.create(2), node.create(3)),
     'expected': node.create(1, node.create(3), node.create(2)), 'reason': 'Tree with multiple nodes1'},
    {'args_in': node.create(1, node.create(2), node.create(3, node.create(3), None)),
     'expected': node.create(1, node.create(3, None, node.create(3)), node.create(2)), 'reason': 'multiple node tree2'},
    {'args_in': node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5))),
     'expected': node.create(1, node.create(3, node.create(5), node.create(4, None, node.create(6))), node.create(2)),
     'reason': 'Tree with multiple nodes3'},
]

for test in test_cases:

    tree = test['args_in']
    expected = test['expected']

    expectedStr = tt.to_string_for_testing(expected)

    a8q2.reflect(tree)

    resultStr = tt.to_string_for_testing(tree)

    if resultStr != expectedStr:
        print('Test failed: reflect(): got "' + resultStr \
              + '" expected "' + expectedStr + '" -- ' + test['reason'])

#### Testing reflection method
test_cases = [
    {'args_in': None, 'expected': None, 'reason': 'Empty tree'},
    {'args_in': node.create(1), 'expected': node.create(1), 'reason': 'Tree with one node'},
    {'args_in': node.create(1, node.create(2), node.create(3)),
     'expected': node.create(1, node.create(3), node.create(2)), 'reason': 'Tree with multiple nodes1'},
    {'args_in': node.create(1, node.create(2), node.create(3, node.create(3), None)),
     'expected': node.create(1, node.create(3, None, node.create(3)), node.create(2)), 'reason': 'multiple node tree2'},
    {'args_in': node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5))),
     'expected': node.create(1, node.create(3, node.create(5), node.create(4, None, node.create(6))), node.create(2)),
     'reason': 'Tree with multiple nodes3'},
]

for test in test_cases:

    tree = test['args_in']
    expected = test['expected']

    expectedStr = tt.to_string_for_testing(expected)

    reflectedTree = a8q2.reflection(tree)

    resultStr = tt.to_string_for_testing(reflectedTree)

    if resultStr != expectedStr:
        print('Test failed: reflection(): got "' + resultStr \
              + '" expected "' + expectedStr + '" -- ' + test['reason'])
    if tree is not None and tree is reflectedTree:
        print('Test failed: reflection(): returned the same tree "' + resultStr \
              + '" -- ' + test['reason'])

print('*** Testing Complete ***')