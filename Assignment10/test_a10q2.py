# CMPT 145: Node-Based Data Structures
#   Linked List ADT test script
#   This version reports progress through the script!
#
#   The script runs two kinds of tests:
#      - unit tests: test one function at a time
#      - integration tests: test how functions work together

import a10q2 as Tb


###############################################################################################

def gen_val(key):
    """Given a key, return a string that can’t be mistaken as the key itself"""
    return 'value_for_'+str(key)


###############################################################################################
def test_0():
    reason = 'Table unit test'
    atable = Tb.Table()
    
    assert atable.is_empty(), reason + ': brand new Table not empty!'
    assert atable.size() == 0, reason + ': brand new Table non zero size!'
    
    
    ###############################################################################################
def test_1():
    reason = 'Table insertion test'
    atable = Tb.Table()
    
    
    keys = [5, 3, 7]
    for vvv in keys:
        flag = atable.insert(vvv, gen_val(vvv))
        assert  flag, reason + ': insertion of key '+str(vvv)+' failed'
    
    assert not atable.is_empty(), reason + ': Table with successful insertions is empty!'
    assert atable.size() == 3, reason + ': Table has wrong size!'
    
    ###############################################################################################
def test_2():
    reason = 'Table membership test'
    atable = Tb.Table()
    
    
    keys = [5, 3, 7]
    for vvv in keys:
        flag = atable.insert(vvv, gen_val(vvv))
    
    for vv in keys:
        flag, newvalue = atable.retrieve(vv)
        assert  flag, reason + ': member could not find key in non-trivial tree after deletion'
        assert  newvalue == gen_val(vv), reason + ': member could not find value in non-trivial tree after deletion'
    
    
    ###############################################################################################
def test_4():
    reason = 'Table update test'
    atable = Tb.Table()
    
    keys = [5, 3, 7]
    for vvv in keys:
        flag = atable.insert(vvv, gen_val(vvv))
    
    for vvv in keys:
        flag = atable.insert(vvv, gen_val(vvv)+'_updated!')
        assert  not flag, reason + ': insertion of key '+str(vvv)+' failed'
    
    assert not atable.is_empty(), reason + ': Table with successful updates is empty!'
    assert atable.size() == len(keys), reason + ': Table has wrong size!'
    
    for vvv in keys:
        flag, newvalue = atable.retrieve(vvv)
        assert flag, reason + ': key '+str(vvv)+' not found after update'
        assert newvalue == gen_val(vvv)+'_updated!', reason + ': value for '+str(vvv)+' not properly updated'
    
    
    ###############################################################################################
def test_5():
    reason = 'Table deletion test'
    atable = Tb.Table()
    
    keys = [5, 3, 10]
    for v in keys:
        atable = Tb.Table()
        for vvv in keys:
            flag = atable.insert(vvv, gen_val(vvv))
    
        flag = atable.delete(v)
        assert  flag, reason + ': deletion of data failed in non-trivial tree'
        flag, newvalue = atable.retrieve(v)
        assert  not flag, reason + ': member found deleted key in non-trivial tree'
        assert  newvalue is None, reason + ': member returned some value in non-trivial tree'
        assert not atable.is_empty(), reason + ': Table with successful insertions is empty!'
        assert atable.size() == len(keys)-1, reason + ': Table has wrong size!'
        for vv in keys:
            if v != vv:
                flag, newvalue = atable.retrieve(vv)
                assert  flag, reason + ': member could not find key in non-trivial tree after deletion'
                assert  newvalue == gen_val(vv), reason + ': member could not find value in non-trivial tree after deletion'
    
    
    ###############################################################################################
def test_6():
    reason = 'Table total annihilation test'
    atable = Tb.Table()
    
    keys = [5, 3, 8, 6, 10, 1, 15, 11, 24, -1]
    for v in keys:
        flag = atable.insert(v, gen_val(v))
    
    assert not atable.is_empty(), reason + ': Table with successful insertions is empty!'
    assert atable.size() == len(keys), reason + ': Table has wrong size!'
    
    for v in keys:
        flag = atable.delete(v)
        assert  flag, reason + ': deletion of data failed in non-trivial tree'
    
    assert atable.is_empty(), reason + ': Table with all keys deleted is not empty'
    assert atable.size() == 0, reason + ': Table has non-zero size!'
    
