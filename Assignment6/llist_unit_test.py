# CMPT 145: Assignment 6
#   Linked List ADT test script
#   This version uses pytest
#      To run from the commandline:
#         UNIX$ pytest
#           - reads any file in the folder with the word test in the name
#           - calls any function with the word test in the function name
#           - looks at assertions, counts the ones that pass and the ones that fail
#           - unlike normal Python, pytest records an assertion failure, but carries on
#           - reports on every assertion that fails!
#           - ends with a summary, e.g,  "== 233 passed in 0.45 seconds =="
#         UNIX$ pytest llist_unit_test.py
#           - reads only the named file, then does the above only for this file
#
#         UNIX$ pytest  --tb=no  llist_unit_test.py
#           - commandline argument NEEDS 2 dashes!  It won't work if you use just one
#           - eliminates almost all of the reporting, just reports progress, and final result
#           - runs all test scripts if no script given on command line
#
#         UNIX$ pytest  --maxfail=10  llist_unit_test.py
#           - commandline argument NEEDS 2 dashes!  It won't work if you use just one
#           - runs all test scripts if no script given on command line
#           - keeps working until 10 test failures are accumulated, then stops
#           - saves you time when you only have completed some of the operations
#           - you can change the value to anything you like
#           - when maxfail=1, you just get the first failure.
#
#     You can configure PyCharm to use pytest for this script:
#          Open the Settings/Preferences | Tools | Python Integrated Tools settings dialog
#          In the Default test runner field select "pytest"  It may appear as "py.test"
#          Click OK to save the settings.
#
#     Now you can choose to run this script using pytest from PyCharm's Run menu!
#     PyCharm will organize the test results in a new interface panel at the bottom
#       You can click on any of the tests, and see the report
#       You can choose to hide or show tests that pass
#       You can choose to let PyCharm run our tests automatically
#
#   The script contains unit tests only
#        * some unit tests look into the LList record
#        * some unit tests construct a record without LList.create()
#      - all tests are allowed to violate the ADT principle, because we're testing it!


import LList as List

###############################################################################################
# UNIT TESTING - List.create()
# These tests should pass using the create() function given in LList
# If you change create() these tests may fail!
###############################################################################################

def test_create_key_size():
    # each test function sets up an independent context for the test
    # here, we use the ADT to create a LList

    allist = List.create()

    # then the test uses assert, giving the test condition and the reason
    # here we check that the record returned has one of the necessary fields

    assert 'size' in allist, "create(): new LList record; 'size' MISSING!"


def test_create_key_head():
    allist = List.create()
    assert 'head' in allist, "create(): Check key 'head' in new LList record; 'head' MISSING!"


def test_create_key_tail():
    allist = List.create()
    assert 'tail' in allist, "create(): Check key 'tail' in new LList record; 'tail' MISSING!"


def test_create_initial_size():
    allist = List.create()
    result = allist['size']
    assert result == 0, "create(): Check size in new LList record; returned "+str(result)


def test_create_initial_head():
    allist = List.create()
    result = allist['head'] 
    assert result is None, "create(): Check head in new LList record; returned "+str(result)


def test_create_initial_tail():
    allist = List.create()
    result = allist['tail'] 
    assert result is None, "create(): Check tail in new LList record; returned "+str(result)


###############################################################################################
# UNIT TESTING - List.empty(), List.size()
###############################################################################################

def test_empty_empty():
    # create a record by hand
    thellist = {'size': 0, 'tail': None, 'head': None}

    # check if is_empty() works
    result = List.is_empty(thellist)
    assert result , 'is_empty() on new LList record; returned '+str(result)


def test_empty_singleton():
    # create a node chain and list by hand
    thenode = {'data': 'arbitrary', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}

    # check if is_empty() works
    result = not List.is_empty(thellist)
    assert result , 'is_empty() on singleton LList; returned '+str(result)


def test_size_singleton():
    thenode = {'data': 'arbitrary', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    result = List.size(thellist) 
    assert result == 1, 'size() on singleton LList; returned '+str(result)


###############################################################################################
# UNIT TESTING - List.add_to_front()
###############################################################################################

def test_add_to_front_size_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = thellist['size'] 
    assert result == 1, 'add_to_front(): check size after insertion on empty LList; returned '+str(result)


def test_add_to_front_head_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = thellist['head'] 
    assert result is not None, 'add_to_front() check head after insertion on empty LList; head not set correctly'


def test_add_to_front_tail_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = thellist['tail'] 
    assert result is not None, 'add_to_front() check head after insertion on empty LList; tail not set correctly'


def test_add_to_front_refs_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = thellist['head'] 
    assert result is thellist['tail'], 'add_to_front() check head, tail after insertion on empty LList; head tail refs should be same but are not'


def test_add_to_front_data_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = thellist['head']['data'] 
    assert result is target, 'add_to_front() check data at head after insertion on empty LList; data set to '+str(result)+' but should be '+"'"+str(target)+"'"


def test_add_to_front_data_2():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = thellist['tail']['data'] 
    assert result is target, 'add_to_front() check data at tail after insertion on empty LList; data set to '+str(result)+' but should be '+"'"+str(target)+"'"


def test_add_to_front_end_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = thellist['head']['next'] 
    assert result is None, 'add_to_front() check node chain after insertion on empty LList: chain should end at one node, but next is not None!'


def test_add_to_front_empty_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'one'
    List.add_to_front(thellist, target)
    result = not List.is_empty(thellist)
    assert result , 'add_to_front() check is_empty() after insertion on empty LList: is_empty() returned True'


###############################################################################################
# UNIT TESTING - List.add_to_front()
###############################################################################################

def test_add_to_front_size_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['size'] 
    assert result == 2, 'add_to_front()  on LList with one node: size not set correctly'


def test_add_to_front_head_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['head'] 
    assert result is not thenode, 'add_to_front()  on LList with one node: head not set correctly'


def test_add_to_front_tail_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['tail'] 
    assert result is thenode, 'add_to_front()  on LList with one node: tail not set correctly'


def test_add_to_front_refs_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['head'] 
    assert result != thellist['tail'], 'add_to_front()  on LList with one node: head tail refs equal'


def test_add_to_front_data_3():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['head']['data'] 
    assert result == target, 'add_to_front()  on LList with one node: data not set correctly in head'


def test_add_to_front_chain_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['head']['next'] 
    assert result is not None, 'add_to_front()  on LList with one node: chain should not end at one node'


def test_add_to_front_chain_3():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['head']['next'] 
    assert result is thenode, 'add_to_front()  on LList with one node: new node should point to existing node'


def test_add_to_front_data_4():
    tail_data = 'not the target'
    thenode = {'data': tail_data, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = thellist['tail']['data'] 
    assert result == tail_data, 'add_to_front()  on LList with one node: data not set correctly in tail'


def test_add_to_front_empty_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = not List.is_empty(thellist)
    assert result , 'add_to_front() on LList with one node; is_empty() returned True'


def test_add_to_front_size_3():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'two'
    List.add_to_front(thellist, target)
    result = List.size(thellist) 
    assert result == 2, 'add_to_front()  on LList with one node: size() not returning correct value'


###############################################################################################
# UNIT TESTING - List.add_to_back()
###############################################################################################

def test_add_to_back_head_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = thellist['head'] 
    assert result is not None, 'add_to_back() check head after insertion on empty LList: head not set correctly'


def test_add_to_back_tail_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = thellist['tail'] 
    assert result is not None, 'add_to_back() check tail after insertion on empty LList: tail not set correctly'


def test_add_to_back_size_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = thellist['size'] 
    assert result == 1, 'add_to_back() check size after insertion on empty LList: size not set correctly'


def test_add_to_back_refs_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = thellist['head'] 
    assert result == thellist['tail'], 'add_to_back() check head, tail after insertion on empty LList: head tail refs different'


def test_add_to_back_data_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = thellist['head']['data'] 
    assert result == target, 'add_to_back() check data at head after insertion on empty LList: data not set correctly in head'


def test_add_to_back_data_2():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = thellist['tail']['data'] 
    assert result == target, 'add_to_back() check data at tail after insertion on empty LList: data not set correctly in tail'


def test_add_to_back_chain_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = thellist['head']['next'] 
    assert result is None, 'add_to_back() check node chain after insertion on empty LList: chain should end at one node'


def test_add_to_back_empty_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = not List.is_empty(thellist)
    assert result , 'add_to_back() check is_empty() after insertion on empty LList: is_empty() returned True'


def test_add_to_back_size_2():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 'three'
    List.add_to_back(thellist, target)
    result = List.size(thellist) 
    assert result == 1, 'add_to_back() check size after insertion on empty LList: size() returned '+str(result)


###############################################################################################
# UNIT TESTING - List.add_to_back()
###############################################################################################

def test_add_to_back_size_3():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['size'] 
    assert result == 2, 'add_to_back() on LList with one node: size not set correctly'


def test_add_to_back_head_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['head'] 
    assert result is thenode, 'add_to_back()  on LList with one node: head not set correctly'


def test_add_to_back_tail_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['tail'] 
    assert result is not None, 'add_to_back()  on LList with one node: tail not set correctly'


def test_add_to_back_tail_3():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['tail'] 
    assert result is not thenode, 'add_to_back()  on LList with one node: tail should be the new node, but is not'


def test_add_to_back_refs_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['head'] 
    assert result != thellist['tail'], 'add_to_back() on LList with one node: head tail refs equal, but should not'


def test_add_to_back_data_3():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['tail']['data'] 
    assert result == target, 'add_to_back() on LList with one node: data not set correctly in tail; should be '+str(target)+'but found '+str(result)


def test_add_to_back_data_4():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['head']['data'] 
    assert result != target, 'add_to_back() on LList with one node: data not set correctly in head; should be '+str(target)+'but found '+str(result)


def test_add_to_back_chain_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = thellist['head']['next'] 
    assert result is not None, 'add_to_back() on LList with one node: chain ended at one node, but should not'


def test_add_to_back_empty_2():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = not List.is_empty(thellist)
    assert result , 'add_to_back() on LList with one node: is_empty() returned True but should not'


def test_add_to_back_size_4():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'four'
    List.add_to_back(thellist, target)
    result = List.size(thellist) 
    assert result == 2, 'add_to_back() on LList with one node: size() returned '+str(result)


###############################################################################################
# UNIT TESTING - List.value_is_in()
###############################################################################################

def test_value_is_in_empty():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 5
    result = List.value_is_in(thellist, target) 
    assert result is False, 'value_is_in() on empty LList; returned True but should not'


def test_value_is_in_false_1():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'six'
    result = List.value_is_in(thellist, target) 
    assert result is False, 'value_is_in() on singleton LList, target not present; returned True but should not'


def test_value_is_in_true_1():
    target = '7'
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    result = List.value_is_in(thellist, target) 
    assert result is True, 'value_is_in() on singleton LList, target present; returned False but should not'


def test_value_is_in_false_2():
    target = '7'
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    result = List.value_is_in(thellist, target) 
    assert result is False, 'value_is_in() on LList with 2 nodes, target not present; returned True but should not'


def test_value_is_in_true_2():
    target = '7'
    thetail = {'data': target, 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    result = List.value_is_in(thellist, target) 
    assert result is True, 'value_is_in() on LList with 2 nodes, target in tail; returned False but should not'


def test_value_is_in_true_3():
    target = '7'
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': target, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    result = List.value_is_in(thellist, target) 
    assert result is True, 'value_is_in() on LList with 2 nodes, target in head; returned False but should not'


###############################################################################################
# UNIT TESTING - List.get_index_of_value()
###############################################################################################

def test_get_index_of_value_empty_flag_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 9
    flag, idx = List.get_index_of_value(thellist, target)
    result = flag 
    assert result is False, 'get_index_of_value() on empty LList; returned True but should not'


def test_get_index_of_value_empty_idx_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    target = 9
    flag, idx = List.get_index_of_value(thellist, target)
    result = idx 
    assert result is None, 'get_index_of_value() on empty LList; returned index that is not None'


def test_get_index_of_value_notempty_flag_1():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'six'
    flag, idx = List.get_index_of_value(thellist, target)
    result = flag 
    assert result is False, 'get_index_of_value() on singleton LList, target not present: returned True but should not'


def test_get_index_of_value_notempty_idx_1():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    target = 'six'
    flag, idx = List.get_index_of_value(thellist, target)
    result = idx 
    assert result is None, 'get_index_of_value() on singleton LList, target not present: returned non-None index'


def test_get_index_of_value_notempty_flag_2():
    target = '10'
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, idx = List.get_index_of_value(thellist, target)
    result = flag 
    assert result is True, 'get_index_of_value() on singleton LList, target present: returned False but should not'


def test_get_index_of_value_notempty_idx_2():
    target = '10'
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, idx = List.get_index_of_value(thellist, target)
    result = idx 
    assert result == 0, 'get_index_of_value() on singleton LList, target present: returned index '+str(result)+', should be 0'


def test_get_index_of_value_notempty_flag_3():
    target = '10'
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    flag, idx = List.get_index_of_value(thellist, target)
    result = flag 
    assert result is False, 'get_index_of_value() on LList with 2 nodes, target not present: returned True'


def test_get_index_of_value_notempty_idx_3():
    target = '10'
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    flag, idx = List.get_index_of_value(thellist, target)
    result = idx 
    assert result is None, 'get_index_of_value() on LList with 2 nodes, target not present: returned non-None index'


def test_get_index_of_value_notempty_flag_4():
    target = '10'
    thetail = {'data': target, 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    flag, idx = List.get_index_of_value(thellist, target)
    result = flag 
    assert result is True, 'get_index_of_value() on LList with 2 nodes, target in tail: returned False'


def test_get_index_of_value_notempty_idx_4():
    target = '10'
    thetail = {'data': target, 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    flag, idx = List.get_index_of_value(thellist, target)
    result = idx 
    assert result == 1, 'get_index_of_value() on LList with 2 nodes, target in tail: returned incorrect index '+str(result)


def test_get_index_of_value_notempty_flag_5():
    target = '10'
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': target, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    flag, idx = List.get_index_of_value(thellist, target)
    result = flag 
    assert result is True, 'get_index_of_value() on LList with 2 nodes, target in head: returned False'


def test_get_index_of_value_notempty_idx_5():
    target = '10'
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': target, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    flag, idx = List.get_index_of_value(thellist, target)
    result = idx 
    assert result == 0, 'get_index_of_value() on LList with 2 nodes, target in head: returned incorrect index '+str(result)


###############################################################################################
# UNIT TESTING - List.retrieve_data_at_index()
###############################################################################################

def test_retrieve_data_at_flag_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = flag 
    assert result is False, 'retrieve_data_at_index() on empty LList: returned True but should not'


def test_retrieve_data_at_val_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = val 
    assert result is None, 'retrieve_data_at_index() on empty LList: returned non-None value'


def test_retrieve_data_at_flag_2():
    target = 12
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = flag 
    assert result is True, 'retrieve_data_at_index() on singleton LList, valid index; returned False but should not'


def test_retrieve_data_at_val_2():
    target = 12
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = val 
    assert result == target, 'retrieve_data_at_index() on singleton LList, valid index; returned '+str(result)+' instead of '+str(target)


def test_retrieve_data_at_flag_3():
    thetail = {'data': 16, 'next': None}
    thehead = {'data': 18, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = flag 
    assert result is True, 'retrieve_data_at_index() on LList with two nodes, index 0: returned False but should not'


def test_retrieve_data_at_val_3():
    target = 18
    thetail = {'data': 16, 'next': None}
    thehead = {'data': target, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = val 
    assert result == target, 'retrieve_data_at_index(): on LList with two nodes, index 0; returned data value '+str(result)+' instead of '+str(target)


def test_retrieve_data_at_flag_4():
    thetail = {'data': 16, 'next': None}
    thehead = {'data': 18, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = flag 
    assert result is True, 'retrieve_data_at_index(): on LList with two nodes, index 1: returned False but should not'


def test_retrieve_data_at_val_4():
    thetail = {'data': 16, 'next': None}
    thehead = {'data': 18, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = val 
    assert result == 16, 'retrieve_data_at_index(): on LList with two nodes, index 0; returned data value '+str(result)+' instead of '+str(target)


def test_retrieve_data_at_flag_5():
    thetail = {'data': 16, 'next': None}
    thehead = {'data': 18, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 2
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = flag 
    assert result is False, 'retrieve_data_at_index(): on LList with two nodes, invalid positive index; returned True but should not'


def test_retrieve_data_at_val_5():
    thetail = {'data': 16, 'next': None}
    thehead = {'data': 18, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 2
    flag, val = List.retrieve_data_at_index(thellist, idx)
    result = val 
    assert result is None, 'retrieve_data_at_index(): on LList with two nodes, invalid positive index; returned non-None value'


###############################################################################################
# UNIT TESTING - List.set_data_at_index()
###############################################################################################

def test_set_data_at_index_empty():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 23
    flag = List.set_data_at_index(thellist, idx, target)
    result = flag 
    assert result is False, 'set_data_at_index() on empty LList; returned True but should not'


def test_set_data_at_index_notempty_flag_1():
    target = 23
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.set_data_at_index(thellist, idx, target)
    result = flag 
    assert result is True, 'set_data_at_index() on singleton LList, valid index; returned False but should not'


def test_set_data_at_index_notempty_data_1():
    target = 23
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.set_data_at_index(thellist, idx, target)
    result = thellist['head']['data'] 
    assert result == target, 'set_data_at_index() on singleton LList, valid index; data not set correctly'


def test_set_data_at_index_notempty_flag_2():
    target = 23
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag = List.set_data_at_index(thellist, idx, target)
    result = flag 
    assert result is True, 'set_data_at_index() on LList with 2 nodes, index 0; returned False but should not'


def test_set_data_at_index_notempty_data_2():
    target = 23
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag = List.set_data_at_index(thellist, idx, target)
    result = thellist['head']['data'] 
    assert result == target, 'set_data_at_index() on LList with 2 nodes, index 0; data not set correctly'


def test_set_data_at_index_notempty_flag_3():
    target = 23
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag = List.set_data_at_index(thellist, idx, target)
    result = flag 
    assert result is True, 'set_data_at_index() on LList with 2 nodes, index 1; returned False but should not'


def test_set_data_at_index_notempty_data_3():
    target = 23
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag = List.set_data_at_index(thellist, idx, target)
    result = thellist['tail']['data'] 
    assert result == target, 'set_data_at_index() on LList with 2 nodes, index 1; data not set correctly'


def test_set_data_at_index_notempty_flag_4():
    target = 23
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 2
    flag = List.set_data_at_index(thellist, idx, target)
    result = flag 
    assert result is False, 'set_data_at_index() on LList with 2 nodes, invalid positive index; returned True but should not'


def test_set_data_at_index_notempty_data_4():
    target = 23
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 2
    flag = List.set_data_at_index(thellist, idx, target)
    result = thellist['head']['data'] 
    assert result == 'not the target', 'set_data_at_index() on LList with 2 nodes, invalid positive index; data at head changed incorrectly'


def test_set_data_at_index_notempty_data_5():
    target = 23
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 2
    flag = List.set_data_at_index(thellist, idx, target)
    result = thellist['tail']['data'] 
    assert result == 'not the target', 'set_data_at_index() on LList with 2 nodes, invalid positive index; data at tail changed incorrectly'


###############################################################################################
# UNIT TESTING - List.remove_from_front()
###############################################################################################

def test_remove_from_front_empty_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    flag, val = List.remove_from_front(thellist)
    result = flag 
    assert result is False, 'remove_from_front() on empty LList: returned True but should not'


def test_remove_from_front_empty_2():
    thellist = {'size': 0, 'tail': None, 'head': None}
    flag, val = List.remove_from_front(thellist)
    result = val 
    assert result is None, 'remove_from_front() on empty LList: returned non-None value'


def test_remove_from_front_notempty_in_flag_1():
    target = 25
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, val = List.remove_from_front(thellist)
    result = flag 
    assert result is True, 'remove_from_front() on singleton LList: returned False but should not'


def test_remove_from_front_notempty_in_val_1():
    target = 25
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, val = List.remove_from_front(thellist)
    result = val 
    assert result == target, 'remove_from_front() on singleton LList: returned '+str(result)+' instead of '+str(target)


def test_remove_from_front_notempty_in_size_1():
    target = 25
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, val = List.remove_from_front(thellist)
    result = thellist['size'] 
    assert result == 0, 'remove_from_front() on singleton LList: incorrect size'


def test_remove_from_front_notempty_in_flag_2():
    thetail = {'data': 29, 'next': None}
    thehead = {'data': 33, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 33
    flag, val = List.remove_from_front(thellist)
    result = flag 
    assert result is True, 'remove_from_front() on LList with 2 nodes; returned False but should not'


def test_remove_from_front_notempty_in_val_2():
    thetail = {'data': 29, 'next': None}
    thehead = {'data': 33, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 33
    flag, val = List.remove_from_front(thellist)
    result = val 
    assert result == target, 'remove_from_front() on LList with 2 nodes; returned '+str(result)+' instead of '+str(target)


def test_remove_from_front_notempty_in_size_2():
    thetail = {'data': 29, 'next': None}
    thehead = {'data': 33, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 33
    flag, val = List.remove_from_front(thellist)
    result = thellist['size'] 
    assert result == 1, 'remove_from_front() on LList with 2 nodes; set incorrect size'


###############################################################################################
# UNIT TESTING - List.remove_from_back()
###############################################################################################

def test_remove_from_back_empty_flag():
    thellist = {'size': 0, 'tail': None, 'head': None}
    flag, val = List.remove_from_back(thellist)
    result = flag 
    assert result is False, 'remove_from_back(): returned True for empty list'


def test_remove_from_back_empty_val():
    thellist = {'size': 0, 'tail': None, 'head': None}
    flag, val = List.remove_from_back(thellist)
    result = val 
    assert result is None, 'remove_from_back(): returned non-None value for empty list'


def test_remove_from_back_singleton_flag():
    target = 25
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, val = List.remove_from_back(thellist)
    result = flag 
    assert result is True, 'remove_from_back():  returned False for singleton list'


def test_remove_from_back_singleton_val():
    target = 25
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, val = List.remove_from_back(thellist)
    result = val 
    assert result == target, 'remove_from_back():  returned incorrect value for singleton list'


def test_remove_from_back_singleton_size():
    target = 25
    thenode = {'data': target, 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    flag, val = List.remove_from_back(thellist)
    result = thellist['size'] 
    assert result == 0, 'remove_from_back():  set incorrect size for singleton list'


def test_remove_from_back_multiple_flag():
    thetail = {'data': 29, 'next': None}
    thehead = {'data': 33, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 29
    flag, val = List.remove_from_back(thellist)
    result = flag 
    assert result is True, 'remove_from_back():  returned False for list size 2'


def test_remove_from_back_multiple_val():
    thetail = {'data': 29, 'next': None}
    thehead = {'data': 33, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 29
    flag, val = List.remove_from_back(thellist)
    result = val 
    assert result == target, 'remove_from_back():  returned incorrect value for list size 2'


def test_remove_from_back_multiple_size():
    thetail = {'data': 29, 'next': None}
    thehead = {'data': 33, 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 29
    flag, val = List.remove_from_back(thellist)
    result = thellist['size'] 
    assert result == 1, 'remove_from_back():  set incorrect size for list size 2'


###############################################################################################
# UNIT TESTING - List.insert_value_at_index()
###############################################################################################

def test_insert_value_at_index_empty_head():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = 'head' in thellist
    assert result , 'insert_value_at_index() could not find head'


def test_insert_value_at_index_empty_tail():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = 'tail' in thellist
    assert result , 'insert_value_at_index() could not find tail'


def test_insert_value_at_index_empty_flag():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() returned False for empty list'


def test_insert_value_at_index_empty_size():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['size'] 
    assert result == 1, 'insert_value_at_index() set incorrect size for empty list'


def test_insert_value_at_index_empty_refs():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head'] 
    assert result == thellist['tail'], 'insert_value_at_index()  head tail refs different'


def test_insert_value_at_index_empty_data_1():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['data'] 
    assert result == target, 'insert_value_at_index() data not set correctly'


def test_insert_value_at_index_empty_data_2():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['tail']['data'] 
    assert result == target, 'insert_value_at_index() data not set correctly'


def test_insert_value_at_index_empty_chain():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    target = 'one'
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['next'] 
    assert result is None, 'insert_value_at_index() chain should end at one node'


def test_insert_value_at_index_singleton_flag():
    target = 'two'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() returned False for singleton list (valid index)'


def test_insert_value_at_index_singleton_data():
    target = 'two'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['data'] 
    assert result == target, 'insert_value_at_index() value not inserted correctly for singleton list (index = 0)'


def test_insert_value_at_index_singleton_chain_1():
    target = 'two'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['next'] 
    assert result is not None, 'insert_value_at_index() chain should have 2 nodes now'


def test_insert_value_at_index_singleton_size():
    target = 'two'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['size'] 
    assert result == 2, 'insert_value_at_index() set incorrect size for singleton list'


def test_insert_value_at_index_singleton_refs_1():
    target = 'two'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head'] 
    assert result != thellist['tail'], 'insert_value_at_index() head tail refs are equal'


def test_insert_value_at_index_singleton_refs_2():
    target = 'two'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['tail']['next'] 
    assert result is None, 'insert_value_at_index() tail should have next == None'


def test_insert_value_at_index_singleton_flag_2():
    target = 'three'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() : returned False for singleton list (valid index)'


def test_insert_value_at_index_singleton_data_2():
    target = 'three'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['data'] 
    assert result != target, 'insert_value_at_index() : head value set incorrectly for singleton list (index = 1)'


def test_insert_value_at_index_singleton_data_3():
    target = 'three'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['tail']['data'] 
    assert result == target, 'insert_value_at_index() : value not inserted correctly for singleton list (index = 1)'


def test_insert_value_at_index_singleton_chain_3():
    target = 'three'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['next'] 
    assert result is not None, 'insert_value_at_index() : chain should have 2 nodes now!'


def test_insert_value_at_index_singleton_size_2():
    target = 'three'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['size'] 
    assert result == 2, 'insert_value_at_index() set incorrect size for singleton list'


def test_insert_value_at_index_singleton_refs_3():
    target = 'three'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head'] 
    assert result != thellist['tail'], 'insert_value_at_index() head tail refs are equal'


def test_insert_value_at_index_singleton_chain_2():
    target = 'three'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['tail']['next'] 
    assert result is None, 'insert_value_at_index() tail should have next == None'


def test_insert_value_at_index_singleton_invalid_flag():
    target = 'four'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = flag 
    assert result is False, 'insert_value_at_index() returned True for singleton list but invalid index'


def test_insert_value_at_index_singleton_invalid_size():
    target = 'four'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['size'] 
    assert result == 1, 'insert_value_at_index() changed size for for singleton list but invalid index'


def test_insert_value_at_index_singleton_invalid_refs():
    target = 'four'
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head'] 
    assert result == thellist['tail'], 'insert_value_at_index() head tail refs changed on invalid index'


def test_insert_value_at_index_multiple_flag_1():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'five'
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() : returned False for list size 2 (valid index)'


def test_insert_value_at_index_multiple_data_1():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'five'
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['data'] 
    assert result == target, 'insert_value_at_index() : value not inserted correctly for list size 2 (index = 0)'


def test_insert_value_at_index_multiple_size_1():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'five'
    idx = 0
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['size'] 
    assert result == 3, 'insert_value_at_index() : set incorrect size for list size 2'


def test_insert_value_at_index_multiple_chain_1():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'five'
    idx = 0
    result = thellist['tail']['next'] 
    assert result is None, 'insert_value_at_index() : list size 2, tail should have next == None'


def test_insert_value_at_index_multiple_flag_2():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'six'
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() returned False for list size 2 (valid index)'


def test_insert_value_at_index_multiple_data_2():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'six'
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['data'] 
    assert result != target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 1)'


def test_insert_value_at_index_multiple_data_3():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'six'
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['next']['data'] 
    assert result == target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 1)'


def test_insert_value_at_index_multiple_size_2():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'six'
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['size'] 
    assert result == 3, 'insert_value_at_index() : set incorrect size for list size 2'


def test_insert_value_at_index_multiple_chain_2():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'six'
    idx = 1
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['tail']['next'] 
    assert result is None, 'insert_value_at_index() : list size 2, tail should have next == None'


def test_insert_value_at_index_flag_3():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'nine'
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = flag 
    assert result is True, 'insert_value_at_index() : returned False for list size 2 (valid index)'


def test_insert_value_at_index_data_4():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'nine'
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['data'] 
    assert result != target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 2)'


def test_insert_value_at_index_data_5():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'nine'
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['head']['next']['data'] 
    assert result != target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 2)'


def test_insert_value_at_index_data_6():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'nine'
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['tail']['data'] 
    assert result == target, 'insert_value_at_index() value not inserted correctly for list size 2 (index = 2)'


def test_insert_value_at_index_size_3():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'nine'
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['size'] 
    assert result == 3, 'insert_value_at_index() set incorrect size for list size 2'


def test_insert_value_at_index_chain_3():
    thetail = {'data': 'not the target', 'next': None}
    thehead = {'data': 'not the target', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    target = 'nine'
    idx = 2
    flag = List.insert_value_at_index(thellist, target, idx)
    result = thellist['tail']['next'] 
    assert result is None, 'insert_value_at_index() list size 2, tail should have next == None'


###############################################################################################
# UNIT TESTING - List.delete_item_at_index()
###############################################################################################

def test_delete_item_at_index_empty_flag():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = flag 
    assert result is False, 'delete_item_at_index() returned True for empty list'


def test_delete_item_at_index_empty_size():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['size'] 
    assert result == 0, 'delete_item_at_index() set incorrect size for empty list'


def test_delete_item_at_index_empty_refs():
    thellist = {'size': 0, 'tail': None, 'head': None}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['head'] 
    assert result == thellist['tail'], 'delete_item_at_index() head tail refs different'


def test_delete_item_at_index_singleton_flag():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = flag 
    assert result is True, 'delete_item_at_index() returned False for singleton list (valid index)'


def test_delete_item_at_index_singleton_head():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['head'] 
    assert result is None, 'delete_item_at_index() value not deleted correctly for singleton list (index = 0)'


def test_delete_item_at_index_singleton_size():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['size'] 
    assert result == 0, 'delete_item_at_index() set incorrect size for singleton list'


def test_delete_item_at_index_singleton_tail():
    thenode = {'data': 'not the target', 'next': None}
    thellist = {'size': 1, 'tail': thenode, 'head': thenode}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['tail'] 
    assert result is None, 'delete_item_at_index() tail should be None'


def test_delete_item_at_index_multiple_flag_1():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = flag 
    assert result is True, 'delete_item_at_index() returned False for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_data_1():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['head']['data'] 
    assert result == 'ten', 'delete_item_at_index() value not deleted correctly for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_size_1():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['size'] 
    assert result == 1, 'delete_item_at_index() set incorrect size for list size 2'


def test_delete_item_at_index_multiple_refs_1():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 0
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['head'] 
    assert result == thellist['tail'], 'delete_item_at_index() head tail should be equal'


def test_delete_item_at_index_multiple_flag_2():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag = List.delete_item_at_index(thellist, idx)
    result = flag 
    assert result is True, 'delete_item_at_index() returned False for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_data_2():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['head']['data'] 
    assert result == 'twelve', 'delete_item_at_index() value not deleted correctly for list size 2 (index = 0)'


def test_delete_item_at_index_multiple_size_2():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['size'] 
    assert result == 1, 'delete_item_at_index() set incorrect size for list size 2'


def test_delete_item_at_index_multiple_refs_2():
    thetail = {'data': 'ten', 'next': None}
    thehead = {'data': 'twelve', 'next': thetail}
    thellist = {'size': 2, 'tail': thetail, 'head': thehead}
    idx = 1
    flag = List.delete_item_at_index(thellist, idx)
    result = thellist['head'] 
    assert result == thellist['tail'], 'delete_item_at_index() head tail should be equal'

if __name__ == '__main__':
    print("Don't run this script in Python -- run it with pytest")
