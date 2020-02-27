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
#   The script contains integration tests: test how functions work together
#      - all tests are allowed to violate the ADT principle, because we're testing it!
#      - do unit testing first!  If your code passes all unit tests, this script will
#        try to catch more sophisticated problems that arise only in more extensive use


import LList as List

###############################################################################################
# INTEGRATION TESTING
###############################################################################################

###############################################################################################
# check if all the operations work after a bunch of data is added using add_to_back()
#

def test_integration_add_to_back_is_empty():
    # an integration test tests how operations work together
    # first set up a list with a bunch of nodes in the node chain

    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)

    # now check if a single aspect worked properly
    result = List.is_empty(thellist)
    assert result is False, "checking is_empty() after add_to_back(); returned True!"


def test_integration_add_to_back_size():
    # identical set up
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)

    # check different aspect
    result = List.size(thellist)
    assert result == 7, "checking size() after add_to_back(), should have size 7, returned "+str(result)


def test_integration_add_to_back_value_is_in():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.value_is_in(thellist, "HEY")
    assert result is True, "checking value_is_in() after add_to_back(), didn't find first data value 'HEY'"


def test_integration_add_to_back_value_is_in_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.value_is_in(thellist, "STOPSIGN")
    assert result is True, "checking value_is_in() after add_to_back(), didn't find second data value 'STOPSIGN'"


def test_integration_add_to_back_value_is_in_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.value_is_in(thellist, "TURTLE")
    assert result is True, "checking value_is_in() after add_to_back(), didn't find last data value 'TURTLE'"


def test_integration_add_to_back_value_is_in_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.value_is_in(thellist, "not in the list")
    assert result is False, "checking value_is_in() after add_to_back(), returned True for data value not in llist"


def test_integration_add_to_back_get_index_of_value_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.get_index_of_value(thellist, "HEY")
    assert result == (True, 0), "checking get_index_of_value() after add_to_back(), didn't find data value 'HEY' at index 0"


def test_integration_add_to_back_get_index_of_value_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.get_index_of_value(thellist, "TURTLE")
    assert result == (True, 6), "checking get_index_of_value() after add_to_back(), didn't find data value 'TURTLE' at index 6"


def test_integration_add_to_back_get_index_of_value_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.get_index_of_value(thellist, "DOING-DOING")
    assert result == (True, 4), "checking get_index_of_value() after add_to_back(), didn't find data value 'DOING-DOING' at index 4"


def test_integration_add_to_back_get_index_of_value_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.get_index_of_value(thellist, "GLOBE")
    assert result == (False, None), "checking get_index_of_value() after add_to_back(), returned "+str(result)+" for value not in llist"


def test_integration_add_to_back_retrieve_data_at_index_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.retrieve_data_at_index(thellist, 6)
    assert result == (True, "TURTLE"), "checking retrieve_data_at_index() after add_to_back(), should have gotten 'TURTLE' from index 6, but got "+str(result)


def test_integration_add_to_back_retrieve_data_at_index_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.retrieve_data_at_index(thellist, 0)
    assert result == (True, "HEY"), "checking retrieve_data_at_index() after add_to_back(), should have gotten 'HEY' from index 0, but got "+str(result)


def test_integration_add_to_back_retrieve_data_at_index_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.retrieve_data_at_index(thellist, 2)
    assert result == (True, "THANK-YOU"), "checking retrieve_data_at_index() after add_to_back(), should have gotten 'THANK-YOU' from index 2, but got "+str(result)


def test_integration_add_to_back_retrieve_data_at_index_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.retrieve_data_at_index(thellist, 7)
    assert result == (False, None), "checking retrieve_data_at_index() after add_to_back(), found something at invalid index: "+str(result)


###############################################################################################
# check if all the operations work after a bunch of data is added using add_to_front()
#

def test_integration_add_to_front_is_empty():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.is_empty(thellist)
    assert result is False, "checking is_empty() after add_to_front(); returned True!"


def test_integration_add_to_front_size():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.size(thellist)
    assert result == 7, "checking size() after add_to_front(), should have size 7, returned "+str(result)


def test_integration_add_to_front_value_is_in_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.value_is_in(thellist, "HEY")
    assert result is True, "checking value_is_in() after add_to_front(), didn't find last data value 'HEY'"


def test_integration_add_to_front_value_is_in_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.value_is_in(thellist, "STOPSIGN")
    assert result is True, "checking value_is_in() after add_to_front(), didn't find data value 'STOPSIGN'"


def test_integration_add_to_front_value_is_in_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.value_is_in(thellist, "TURTLE")
    assert result is True, "checking value_is_in() after add_to_front(), didn't find first data value 'TURTLE'"


def test_integration_add_to_front_value_is_in_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.value_is_in(thellist, "not in the list")
    assert result is False, "checking value_is_in() after add_to_front(), returned True for data value not in llist"


def test_integration_add_to_front_get_index_of_value_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.get_index_of_value(thellist, "HEY")
    assert result == (True, 6), "checking get_index_of_value() after add_to_front(), didn't find data value 'HEY' at index 6"


def test_integration_add_to_front_get_index_of_value_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.get_index_of_value(thellist, "TURTLE")
    assert result == (True, 0), "checking get_index_of_value() after add_to_front(), didn't find data value 'TURTLE' at index 0"


def test_integration_add_to_front_get_index_of_value_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.get_index_of_value(thellist, "DOING-DOING")
    assert result == (True, 2), "checking get_index_of_value() after add_to_front(), DOING-DOING is at index 2"


def test_integration_add_to_front_get_index_of_value_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.get_index_of_value(thellist, "GLOBE")
    assert result == (False, None), "checking get_index_of_value() after add_to_front(), GLOBE Not in llist"


def test_integration_add_to_front_retrieve_data_at_index_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.retrieve_data_at_index(thellist, 0)
    assert result == (True, "TURTLE"), "checking get_index_of_value() after add_to_front(), TURTLE is at index 0"


def test_integration_add_to_front_retrieve_data_at_index_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.retrieve_data_at_index(thellist, 6)
    assert result == (True, "HEY"), "checking retrieve_data_at_index() after add_to_front(), HEY is at index 6"


def test_integration_add_to_front_retrieve_data_at_index_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.retrieve_data_at_index(thellist, 3)
    assert result == (True, "TURN-AROUND"), "checking retrieve_data_at_index() after add_to_front(), TURN-AROUND is at index 3"


def test_integration_add_to_front_retrieve_data_at_index_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    result = List.retrieve_data_at_index(thellist, 7)
    assert result == (False, None), "checking retrieve_data_at_index() after add_to_front(), index not valid"


###############################################################################################
# check what happens if you change the data in the Llist using set_data_at_index()

def test_integration_set_data_check_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.set_data_at_index(thellist, 0, "now")
    assert result is True, "checking set_data_at_index() after add_to_back(), index valid"


def test_integration_set_data_get_index_of_value_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 0, "now")
    result = List.get_index_of_value(thellist, "HEY")
    assert result == (False, None), "checking get_index_of_value() after set_data_at_index(), tried to change first data value, but still found original value"


def test_integration_set_data_get_index_of_value_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 0, "now")
    result = List.get_index_of_value(thellist, "now")
    assert result == (True, 0), "checking get_index_of_value() after set_data_at_index(), tried to change first data value, but could not find new value"


def test_integration_set_data_get_index_of_value_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 0, "now")
    result = List.get_index_of_value(thellist, "STOPSIGN")
    assert result == (True, 1), "checking get_index_of_value() after set_data_at_index(), tried to change second data value, but got "+str(result)



def test_integration_set_data_get_index_of_value_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 0, "now")
    result = List.get_index_of_value(thellist, "TURTLE")
    assert result == (True, 6), "checking get_index_of_value() after set_data_at_index(),  'TURTLE' should be still at index 6"


def test_integration_set_data_size_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 0, "now")
    result = List.size(thellist)
    assert result == 7, "checking size() after set_data_at_index(), should have size 7, but got "+str(result)


def test_integration_set_data_get_index_of_check_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.set_data_at_index(thellist, 6, "SIGN")
    assert result is True, "checking set_data_at_index() after add_to_back(), tried to change last data value but returned False"


def test_integration_set_data_get_index_of_value_5():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 6, "SIGN")
    result = List.get_index_of_value(thellist, "TURTLE")
    assert result == (False, None), "checking set_data_at_index() after add_to_back(), TURTLE should be gone, but it's not"


def test_integration_set_data_get_index_of_value_6():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 6, "SIGN")
    result = List.get_index_of_value(thellist, "SIGN")
    assert result == (True, 6), "checking set_data_at_index() after add_to_back(), should have found SIGN at index 6"


def test_integration_set_data_get_index_of_value_7():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 6, "SIGN")
    result = List.get_index_of_value(thellist, "HEY")
    assert result == (True, 0), "checking set_data_at_index() after add_to_back(), HEY should be still at index 0, but returned "+str(result)


def test_integration_set_data_get_index_of_value_8():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 6, "SIGN")
    result = List.get_index_of_value(thellist, "HORSESHOE")
    assert result == (True, 5), "checking set_data_at_index() after add_to_back(), HORSESHOE should be still at index 5"


def test_integration_set_data_get_index_of_size_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 6, "SIGN")
    result = List.size(thellist)
    assert result == 7, "checking size() after set_data_at_index() after add_to_back(), should have size 7"


def test_integration_set_data_get_index_of_check_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.set_data_at_index(thellist, 3, "FOLLOWER")
    assert result is True, "checking set_data_at_index() after add_to_back(): got a False when index valid"


def test_integration_set_data_get_index_of_value_9():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 3, "FOLLOWER")
    result = List.get_index_of_value(thellist, "TURN-AROUND")
    assert result == (False, None), "checking get_index_of_value() after add_to_front(), TURN-AROUND should be gone"


def test_integration_set_data_get_index_of_value_10():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 3, "FOLLOWER")
    result = List.get_index_of_value(thellist, "FOLLOWER")
    assert result == (True, 3), "checking get_index_of_value() after add_to_front(), FOLLOWER should be at index 3"


def test_integration_set_data_get_index_of_size_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.set_data_at_index(thellist, 3, "FOLLOWER")
    result = List.size(thellist)
    assert result == 7, "checking size() after set_data_at_index(), should have size 7"


###############################################################################################
# check what happens as a bunch of insert_value_at() operations are used on a LList

def test_integration_insert_value_at_index_check_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.insert_value_at_index(thellist, "LEFT", 0)
    assert result is True, "index valid"


def test_integration_insert_value_at_index_get_index_of_value_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    result = List.get_index_of_value(thellist, "LEFT")
    assert result == (True, 0), "LEFT is first"


def test_integration_insert_value_at_index_get_index_of_value_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    result = List.get_index_of_value(thellist, "DOING-DOING")
    assert result == (True, 5), "DOING-DOING is at index 5"


def test_integration_insert_value_at_index_size_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    result = List.size(thellist)
    assert result == 8, "should have size 8"


def test_integration_insert_value_at_index_check_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    result = List.insert_value_at_index(thellist, "RIGHT", 8)
    assert result is True, "index valid"


def test_integration_insert_value_at_index_get_index_of_value_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    List.insert_value_at_index(thellist, "RIGHT", 8)
    result = List.get_index_of_value(thellist, "RIGHT")
    assert result == (True, 8), "RIGHT is last"


def test_integration_insert_value_at_index_get_index_of_value_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    List.insert_value_at_index(thellist, "RIGHT", 8)
    result = List.get_index_of_value(thellist, "TURTLE")
    assert result == (True, 7), "TURTLE is at index 7"


def test_integration_insert_value_at_index_size_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    List.insert_value_at_index(thellist, "RIGHT", 8)
    result = List.size(thellist)
    assert result == 9, ": should have size 9"


def test_integration_insert_value_at_index_check_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    List.insert_value_at_index(thellist, "RIGHT", 8)
    result = List.insert_value_at_index(thellist, "MIDDLE", 5)
    assert result is True, "index valid"


def test_integration_insert_value_at_index_get_index_of_value_5():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    List.insert_value_at_index(thellist, "RIGHT", 8)
    List.insert_value_at_index(thellist, "MIDDLE", 5)
    result = List.get_index_of_value(thellist, "MIDDLE")
    assert result == (True, 5), "MIDDLE is at index 5"


def test_integration_insert_value_at_index_get_index_of_value_6():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    List.insert_value_at_index(thellist, "RIGHT", 8)
    List.insert_value_at_index(thellist, "MIDDLE", 5)
    result = List.get_index_of_value(thellist, "TURTLE")
    assert result == (True, 8), "TURTLE is at index 8"


def test_integration_insert_value_at_index_size_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.insert_value_at_index(thellist, "LEFT", 0)
    List.insert_value_at_index(thellist, "RIGHT", 8)
    List.insert_value_at_index(thellist, "MIDDLE", 5)
    result = List.size(thellist)
    assert result == 10, "should have size 10"


###############################################################################################
# check what happens when you start deleting values from the LList

def test_integration_delete_item_at_index_check_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    result = List.delete_item_at_index(thellist, 0)
    assert result is True, "index valid"


def test_integration_delete_item_at_index_get_index_of_value_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    result = List.get_index_of_value(thellist, "HEY")
    assert result == (False, None), "HEY should be gone"


def test_integration_delete_item_at_index_value_is_in_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    result = List.value_is_in(thellist, "HEY")
    assert result is False, "HEY should be gone"


def test_integration_delete_item_at_index_size_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    result = List.size(thellist)
    assert result == 6, "should have size 6"


def test_integration_delete_item_at_index_get_index_of_value_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    result = List.get_index_of_value(thellist, "STOPSIGN")
    assert result == (True, 0), "STOPSIGN should be at index 0"


def test_integration_delete_item_at_index_check_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    result = List.delete_item_at_index(thellist, 5)
    assert result is True, "index valid"


def test_integration_delete_item_at_index_get_index_of_value_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    result = List.get_index_of_value(thellist, "TURTLE")
    assert result == (False, None), "TURTLE should be gone"


def test_integration_delete_item_at_index_value_is_in_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    result = List.value_is_in(thellist, "TURTLE")
    assert result is False, "TURTLE should be gone"


def test_integration_delete_item_at_index_size_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    result = List.size(thellist)
    assert result == 5, "should have size 5"


def test_integration_delete_item_at_index_get_index_of_value_4():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    result = List.get_index_of_value(thellist, "HORSESHOE")
    assert result == (True, 4), "HORSESHOE should be at index 4"


def test_integration_delete_item_at_index_check_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    result = List.delete_item_at_index(thellist, 2)
    assert result is True, "index valid"


def test_integration_delete_item_at_index_get_index_of_value_5():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    List.delete_item_at_index(thellist, 2)
    result = List.get_index_of_value(thellist, "TURN-AROUND")
    assert result == (False, None), "TURN-AROUND should be gone"


def test_integration_delete_item_at_index_value_is_in_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    List.delete_item_at_index(thellist, 2)
    result = List.value_is_in(thellist, "TURN-AROUND")
    assert result is False, "TURN-AROUND should be gone"


def test_integration_delete_item_at_index_size_3():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    List.delete_item_at_index(thellist, 2)
    result = List.size(thellist)
    assert result == 4, "should have size 4"


def test_integration_delete_item_at_index_get_index_of_value_6():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    List.delete_item_at_index(thellist, 0)
    List.delete_item_at_index(thellist, 5)
    List.delete_item_at_index(thellist, 2)
    result = List.get_index_of_value(thellist, "DOING-DOING")
    assert result == (True, 2), "DOING-DOING should be at index 2"


###############################################################################################
# check what happens when you add and remove a bunch from the back

def test_integration_remove_from_back_size():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    for i in range(4):
        List.remove_from_back(thellist)
    result = List.size(thellist)
    assert result == 3, "should have size 3"


def test_integration_remove_from_back_get_index_of_value_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    for i in range(4):
        List.remove_from_back(thellist)
    result = List.get_index_of_value(thellist, "TURN-AROUND")
    assert result == (False, None), "TURN-AROUND should be gone"


def test_integration_remove_from_back_get_index_of_value_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    for i in range(4):
        List.remove_from_back(thellist)
    result = List.get_index_of_value(thellist, "THANK-YOU")
    assert result == (True, 2), "THANK-YOU should be at index 2"


def test_integration_remove_from_back_retrieve_data_at_index_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_back(thellist, word)
    for i in range(4):
        List.remove_from_back(thellist)
    result = List.retrieve_data_at_index(thellist, 2)
    assert result == (True, "THANK-YOU"), "THANK-YOU is at index 2"


###############################################################################################
# check what happens when you add and remove a bunch from the front

def test_integration_remove_from_front_size():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    for i in range(4):
        List.remove_from_front(thellist)
    result = List.size(thellist)
    assert result == 3, "should have size 3"


def test_integration_remove_from_front_get_index_of_value_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    for i in range(4):
        List.remove_from_front(thellist)
    result = List.get_index_of_value(thellist, "TURN-AROUND")
    assert result == (False, None), "TURN-AROUND should be gone"


def test_integration_remove_from_front_get_index_of_value_2():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    for i in range(4):
        List.remove_from_front(thellist)
    result = List.get_index_of_value(thellist, "THANK-YOU")
    assert result == (True, 0), "THANK-YOU should be at index 0"


def test_integration_remove_from_front_retrieve_data_at_index_1():
    thellist = List.create()
    stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
    for word in stuff:
        List.add_to_front(thellist, word)
    for i in range(4):
        List.remove_from_front(thellist)
    result = List.retrieve_data_at_index(thellist, 0)
    assert result == (True, "THANK-YOU"), "THANK-YOU is at index 0"

if __name__ == '__main__':
    print("Don't run this script in Python -- run it with pytest")
