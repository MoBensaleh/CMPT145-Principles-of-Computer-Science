# Mohamed Bensaleh
# CMPT 145 Assignment 8
# 11254030
# Mob127

import a8q1 as a8q1
import treenode as node
import treetesting as tt



#### Testing count_node_types method
test_cases = [
    {'args_in': [node.create(1, node.create(2), node.create(3))],
     'expected': (2,1), 'reason': 'Tree with 2 leaf nodes'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(3), None))],
     'expected': (2,2), 'reason': 'tree with 2 leaf nodes and 2 non-leaf nodes'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5)))],
     'expected': (3,3),
     'reason': 'Tree with 3 leaf and non leaf nodes'},
]

for test in test_cases:
    args = test['args_in']
    expected = test['expected']
    result = a8q1.count_node_types(args[0])

    if result != expected:
        print('Test failed: count_node_types(): got "' + str(result) \
              + '" expected "' + str(expected) + '" -- ' + test['reason'])

#### Testing subst() method
test_cases = [
    {'args_in': [node.create(1, node.create(2), node.create(3)), 2, 9],
     'expected': None, 'reason': 'Target value and replacement in the middle'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(3), None)), 3, 10],
     'expected': None, 'reason': '2 values replaced near the end of the tree'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5))), 1, 7],
     'expected': None,
     'reason': '1 value replaced near the front of the tree'},
]

for test in test_cases:
    args = test['args_in']
    expected = test['expected']
    result = a8q1.subst(args[0], args[1], args[2])

    if result != expected:
        print('Test failed: subst(): got "' + str(result) \
              + '" expected "' + str(expected) + '" -- ' + test['reason'])

#### Testing copy method
test_cases = [
    {'args_in': None, 'expected': None, 'reason': 'Empty tree'},
    {'args_in': node.create(1), 'expected': node.create(1), 'reason': 'Tree with one node'},
    {'args_in': node.create(1, node.create(2), node.create(3)),
     'expected': node.create(1, node.create(2), node.create(3)), 'reason': 'Tree with multiple nodes'},
    {'args_in': node.create(1, node.create(2), node.create(3, node.create(3), None)),
     'expected': node.create(1, node.create(2), node.create(3, node.create(3), None)), 'reason': 'multiple node tree'},
    {'args_in': node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5))),
     'expected': node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5))),
     'reason': 'Tree with multiple nodes'},
]

for test in test_cases:

    tree = test['args_in']
    expected = test['expected']

    expectedStr = tt.to_string_for_testing(expected)

    reflectedTree = a8q1.copy(tree)

    resultStr = tt.to_string_for_testing(reflectedTree)

    if resultStr != expectedStr:
        print('Test failed: copy(): got "' + resultStr \
              + '" expected "' + expectedStr + '" -- ' + test['reason'])

#### Testing nodes_at_level method
test_cases = [
    {'args_in': [node.create(1, node.create(2), node.create(3)), 1],
     'expected': 2, 'reason': 'Tree with 3 nodes at given level 1'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(3), None)), 2],
     'expected': 1, 'reason': 'tree with 4 nodes at given level 2'},
    {'args_in': [node.create(1, node.create(2), node.create(3, node.create(4, node.create(6)), node.create(5))), 2],
     'expected': 2,
     'reason': 'Tree with 6 nodes at given level 2'},
]

for test in test_cases:
    args = test['args_in']
    expected = test['expected']
    result = a8q1.nodes_at_level(args[0], args[1])

    if result != expected:
        print('Test failed: nodes_at_level(): got "' + str(result) \
              + '" expected "' + str(expected) + '" -- ' + test['reason'])

print('***Testing Complete***')