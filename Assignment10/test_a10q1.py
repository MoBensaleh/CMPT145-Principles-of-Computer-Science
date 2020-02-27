# CMPT 145: Testing suite for A10Q1

# This file is copyright (c) Michael C Horsch, provided solely for the
# use of CMPT 145 students.  Students are welcome to use this file
# for their own work, and make copies for their own personal use.
# This file should not be shared for any reason without explicit
# consent of the author.



import a10q1 as KV


def gen_val(key):
    """
    Purpose:
        Given a key, return a string that can’t be mistaken as the key itself.
        This will help us detect errors if a key is added or changed instead of a
        data value
    Return:
        a string based on key
    """
    return 'value_for_key_' + str(key)


def str_form(obj, result, exp, reason):
    """
    Purpose:
        Abbreviate test case assertions.
    Preconditions:
        :param obj:  a string
        :param result: a value
        :param reason: a string
    :return: a string
    """
    return ' '.join(['Test fault:', obj,
                     'returned', str(result),
                     '(expected:', str(exp) + ')',
                     'on:', reason])


###############################################################################################


def test_0():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    result, newtree = KV.insert_prim(atnode, key, value)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_1():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, check tree'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, result = KV.insert_prim(atnode, key, value)
    assert result is not None, str_form(test_objective, None, 'not None', reason)


def test_2():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, check tree key'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atree = KV.insert_prim(atnode, key, value)
    result = atree.key
    expected = key
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_3():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, check tree value'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)
    result = atnode.value
    expected = value
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_3a():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change tree value, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    value = str('this is new')
    result, newtree = KV.insert_prim(atnode, key, value)
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_3b():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change tree value, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    value = str('this is new')
    flag, result = KV.insert_prim(atnode, key, value)
    assert result is not None, str_form(test_objective, None, 'not None', reason)


def test_3c():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change tree value, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    value = str('this is new')
    flag, atnode = KV.insert_prim(atnode, key, value)
    result = atnode.value
    expected = value
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_00():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert left, check flag'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 3
    value = gen_val(key)
    result, newtree = KV.insert_prim(atnode, key, value)

    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_01():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert left, check tree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 3
    value = gen_val(key)
    flag, result = KV.insert_prim(atnode, key, value)

    expected = atnode

    assert result == expected, str_form(test_objective, 'different reference', 'reference to original tree', reason)


def test_02():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert left, check root key'

    atnode = None
    rkey = 5
    value = gen_val(rkey)
    flag, atnode = KV.insert_prim(atnode, rkey, value)

    key = 3
    value = gen_val(key)
    flag, result = KV.insert_prim(atnode, key, value)

    result = atnode.key
    expected = rkey
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_03():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert left, check root value'
    atnode = None

    rkey = 5
    rvalue = gen_val(rkey)
    flag, atnode = KV.insert_prim(atnode, rkey, rvalue)

    key = 3
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result = atnode.value
    expected = rvalue
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_04():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert left, check left tree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 3
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result = atnode.left

    assert result is not None, str_form(test_objective, None, 'something non None', reason)


def test_04a():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert left, check right tree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 3
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result = atnode.right

    assert result is None, str_form(test_objective, 'something non None', None, reason)


def test_03a():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change left value, check flag'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 3
    lvalue = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, lvalue)

    nvalue = str('this is new')
    result, newtree = KV.insert_prim(atnode, lkey, nvalue)
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_03b():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change left value, check left subtree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 3
    lvalue = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, lvalue)

    value = str('this is new')
    flag, result = KV.insert_prim(atnode, key, value)
    assert result is not None, str_form(test_objective, None, 'not None', reason)


def test_03c():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change left value, check left value'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 8
    lvalue = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, lvalue)

    value = str('this is new')
    flag, atnode = KV.insert_prim(atnode, key, value)
    result = atnode.value
    expected = value
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_03d():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change right value, check flag'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 8
    lvalue = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, lvalue)

    nvalue = str('this is new')
    result, newtree = KV.insert_prim(atnode, lkey, nvalue)
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_03e():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change right value, check right subtree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 8
    lvalue = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, lvalue)

    value = str('this is new')
    flag, result = KV.insert_prim(atnode, key, value)
    assert result is not None, str_form(test_objective, None, 'not None', reason)


def test_03f():
    test_objective = 'insert_prim()'
    reason = 'empty kvtree, change right value, check right value'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 3
    lvalue = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, lvalue)

    value = str('this is new')
    flag, atnode = KV.insert_prim(atnode, key, value)
    result = atnode.value
    expected = value
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_000():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert right, check flag'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 8
    value = gen_val(key)
    result, newtree = KV.insert_prim(atnode, key, value)

    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_001():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert right, check tree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 8
    value = gen_val(key)
    flag, result = KV.insert_prim(atnode, key, value)

    expected = atnode

    assert result == expected, str_form(test_objective, 'different reference', 'reference to original tree', reason)


def test_002():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert right, check root key'

    atnode = None
    rkey = 5
    value = gen_val(rkey)
    flag, atnode = KV.insert_prim(atnode, rkey, value)

    key = 8
    value = gen_val(key)
    flag, result = KV.insert_prim(atnode, key, value)

    result = atnode.key
    expected = rkey
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_003():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert left, check root value'
    atnode = None

    rkey = 5
    rvalue = gen_val(rkey)
    flag, atnode = KV.insert_prim(atnode, rkey, rvalue)

    key = 8
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result = atnode.value
    expected = rvalue
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_004():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert right, check right tree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 8
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result = atnode.right

    assert result is not None, str_form(test_objective, None, 'something non None', reason)


def test_004a():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert right, check left tree'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    key = 8
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result = atnode.left

    assert result is None, str_form(test_objective, 'something non None', None, reason)


def test_005():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert right, check right key'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 8
    value = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, value)

    result = atnode.right.key
    expected = lkey
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_006():
    test_objective = 'insert_prim()'
    reason = 'singleton kvtree, insert right, check right value'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    lkey = 8
    lvalue = gen_val(lkey)
    flag, atnode = KV.insert_prim(atnode, lkey, lvalue)

    result = atnode.right.value
    expected = lvalue
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_hint_0():
    test_objective = """
    Several bugs were added to bstprim:
        Several locations where 'is' is used.  Does it matter?
        Lines 44, 45, 47.
        Lines 74, 75.
        Lines 77, 83
    If you find this hint, don't shout it out to everyone.
    Maybe tell people that you found it useful to read the test script.
    """
    assert True, test_objective


def test_4():
    test_objective = 'member_prim()'
    reason = 'singleton kvtree, value at root, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result, retval = KV.member_prim(atnode, key)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_5():
    test_objective = 'member_prim()'
    reason = 'singleton kvtree, value at root, check value'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    flag, result = KV.member_prim(atnode, key)
    expected = value
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_6():
    test_objective = 'member_prim()'
    reason = 'singleton kvtree, value not in tree, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result, retval = KV.member_prim(atnode, 'kjsdhkjsdhgsdfkjghdfkgjhsdkjhfsdg')
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7():
    test_objective = 'member_prim()'
    reason = 'singleton kvtree, value not in tree, check value'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    flag, result = KV.member_prim(atnode, 'kjsdhkjsdhgsdfkjghdfkgjhsdkjhfsdg')
    expected = None
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7b():
    test_objective = 'member_prim()'
    reason = 'tree with left child, value in left child, check flag'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    skey = 3
    value = gen_val(skey)
    flag, atnode = KV.insert_prim(atnode, skey, value)

    result, retval = KV.member_prim(atnode, skey)
    expected = True

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7c():
    test_objective = 'member_prim()'
    reason = 'tree with left child, value in left child, check value'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    skey = 3
    svalue = gen_val(skey)
    flag, atnode = KV.insert_prim(atnode, skey, svalue)

    flag, result = KV.member_prim(atnode, skey)
    expected = svalue

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7d():
    test_objective = 'member_prim()'
    reason = 'tree with right child, value in right child, check flag'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    skey = 8
    value = gen_val(skey)
    flag, atnode = KV.insert_prim(atnode, skey, value)

    result, retval = KV.member_prim(atnode, skey)
    expected = True

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7e():
    test_objective = 'member_prim()'
    reason = 'tree with right child, value in right child, check value'
    atnode = None

    key = 5
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    skey = 8
    svalue = gen_val(skey)
    flag, atnode = KV.insert_prim(atnode, skey, svalue)

    flag, result = KV.member_prim(atnode, skey)
    expected = svalue

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7f():
    test_objective = 'member_prim()'
    reason = 'voluminous tree, value in tree to left'
    atnode = None

    keys = [10, 5, 15, 3, 7, 12, 17, 4, 6, 16, 25, 20]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    skey = 3
    svalue = gen_val(skey)
    flag, result = KV.member_prim(atnode, skey)
    expected = svalue

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7g():
    test_objective = 'member_prim()'
    reason = 'voluminous tree, value in tree to right'
    atnode = None

    keys = [10, 5, 15, 3, 7, 12, 17, 4, 6, 16, 25, 20]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    skey = 16
    svalue = gen_val(skey)
    flag, result = KV.member_prim(atnode, skey)
    expected = svalue

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_7h():
    test_objective = 'member_prim()'
    reason = 'voluminous tree, value not in tree'
    atnode = None

    keys = [10, 5, 15, 3, 7, 12, 17, 4, 6, 16, 25, 20]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    skey = 3333333333
    svalue = gen_val(skey)
    flag, result = KV.member_prim(atnode, skey)
    expected = None

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_8():
    test_objective = 'delete_prim()'
    reason = 'singleton kvtree, value at root, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result, retval = KV.delete_prim(atnode, key)
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_9():
    test_objective = 'delete_prim()'
    reason = 'singleton kvtree, value at root, check resulting tree'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    flag, result = KV.delete_prim(atnode, key)
    expected = None
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_10():
    test_objective = 'delete_prim()'
    reason = 'singleton kvtree, value not in tree, check flag'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    result, retval = KV.delete_prim(atnode, 'kjsdhkjsdhgsdfkjghdfkgjhsdkjhfsdg')
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_11():
    test_objective = 'delete_prim()'
    reason = 'singleton kvtree, value not in tree, check resulting tree'
    atnode = None
    key = 'one'
    value = gen_val(key)
    flag, atnode = KV.insert_prim(atnode, key, value)

    flag, result = KV.delete_prim(atnode, 'kjsdhkjsdhgsdfkjghdfkgjhsdkjhfsdg')
    expected = atnode
    assert result == expected, str_form(test_objective, 'some tree', 'not the expected tree', reason)


def test_12():
    test_objective = 'delete_prim()'
    reason = '2 level tree, left leaf, check flag'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    result, newtree = KV.delete_prim(atnode, 3)
    expected = True

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_13():
    test_objective = 'delete_prim()'
    reason = '2 level tree, left leaf, check resulting tree'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, result = KV.delete_prim(atnode, 3)

    assert result is not None, str_form(test_objective, None, 'something non None', reason)


def test_14():
    test_objective = 'delete_prim()'
    reason = '2 level tree, left leaf, check left subtree'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 3)

    result = atnode.left
    assert result is None, str_form(test_objective, 'something non None', None, reason)


def test_15():
    test_objective = 'delete_prim()'
    reason = '2 level tree, left leaf, check right subtree'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 3)

    result = atnode.right

    assert result is not None, str_form(test_objective, None, 'something non None', reason)


def test_12a():
    test_objective = 'delete_prim()'
    reason = '2 level tree, right leaf, check flag'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    result, newtree = KV.delete_prim(atnode, 7)
    expected = True

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_13b():
    test_objective = 'delete_prim()'
    reason = '2 level tree, right leaf, check resulting tree'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, result = KV.delete_prim(atnode, 7)

    assert result is not None, str_form(test_objective, None, 'something non None', reason)


def test_14b():
    test_objective = 'delete_prim()'
    reason = '2 level tree, right leaf, check left subtree'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 7)

    result = atnode.left
    assert result is not None, str_form(test_objective, None, 'a non-empty tree', reason)


def test_15b():
    test_objective = 'delete_prim()'
    reason = '2 level tree, right leaf, check right subtree'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 7)

    result = atnode.right

    assert result is None, str_form(test_objective, 'something non None', None, reason)


def test_12c():
    test_objective = 'delete_prim()'
    reason = '2 level tree, root, check flag'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    result, newtree = KV.delete_prim(atnode, 5)
    expected = True

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_13c():
    test_objective = 'delete_prim()'
    reason = '2 level tree, root, check resulting tree'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, result = KV.delete_prim(atnode, 5)

    assert result is not None, str_form(test_objective, None, 'something non None', reason)


def test_14c():
    test_objective = 'delete_prim()'
    reason = '2 level tree, root, check former left key'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 5)

    result, retval = KV.member_prim(atnode, 3)
    expected = True

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_14d():
    test_objective = 'delete_prim()'
    reason = '2 level tree, root, check former left value'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 5)

    flag, result = KV.member_prim(atnode, 3)
    expected = gen_val(3)

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_14e():
    test_objective = 'delete_prim()'
    reason = '2 level tree, root, check right key'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 5)

    result, retval = KV.member_prim(atnode, 7)
    expected = True

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_14f():
    test_objective = 'delete_prim()'
    reason = '2 level tree, root, check right value'
    atnode = None

    keys = [5, 3, 7]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))

    flag, atnode = KV.delete_prim(atnode, 5)

    flag, result = KV.member_prim(atnode, 7)
    expected = gen_val(7)

    assert result == expected, str_form(test_objective, result, expected, reason)


def test_20():
    test_objective = 'insert_prim() + member_prim()'
    reason = 'voluminous tree, all keys, check all values'
    atnode = None

    keys = [10, 5, 15, 3, 7, 12, 17, 4, 6, 16, 25, 20]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))
        assert flag, str_form(test_objective, False, True, reason + ': sequential insertion into tree failed')

    for v in keys:
        retflag, retval = KV.member_prim(atnode, v)
        expected = True
        assert retflag == expected, str_form(test_objective, retflag, expected,
                                             reason + ' failed to find key ' + str(k))
        expected = gen_val(v)
        assert retval == expected, str_form(test_objective, retval, expected, reason + ' failed to find data value')


def test_21():
    test_objective = 'insert_prim() + member_prim()'
    reason = 'voluminous tree, all keys, check values not in tree'
    atnode = None

    keys = [10, 5, 15, 3, 7, 12, 17, 4, 6, 16, 25, 20]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))
        assert flag, str_form(test_objective, False, True, reason + ': sequential insertion into tree failed')

    for v in [8, 19, 0, 44]:
        retflag, retval = KV.member_prim(atnode, v)
        expected = False
        assert retflag == expected, str_form(test_objective, retflag, expected,
                                             reason + ': unexpected success for key' + str(k))
        expected = None
        assert retval == expected, str_form(test_objective, retval, expected,
                                            reason + ': found data value ' + str(retval))


def test_22():
    test_objective = 'insert_prim() + delete_prim()'
    reason = 'voluminous tree, all keys, delete each single value'

    keys = [5, 3, 1, 8, 10, 7, 2]

    for k in keys:
        atnode = None

        # create a tree from scratch with all the keys
        for k2 in keys:
            flag, atnode = KV.insert_prim(atnode, k2, gen_val(k2))
            assert flag, str_form(test_objective, False, True, reason + ': sequential insertion into tree failed')

        # remove just the one key k
        retflag, retval = KV.delete_prim(atnode, k)
        expected = True
        assert retflag == expected, str_form(test_objective, retflag, expected,
                                             reason + ': failed to find key ' + str(k))

        # check that the others are all still there
        for v in keys:
            if v != k:
                retflag, retval = KV.member_prim(atnode, v)
                expected = True
                assert retflag == expected, str_form(test_objective, retflag, expected,
                                                     reason + ': failed to find key ' + str(k))
                expected = gen_val(v)
                assert retval == expected, str_form(test_objective, retval, expected,
                                                    reason + ': failed to find data value')


def test_23():
    test_objective = 'insert_prim() + delete_prim()'
    reason = 'voluminous tree, all keys, check values not in tree'
    atnode = None

    keys = [5, 3, 1, 8, 10, 7, 2]

    for k in keys:
        flag, atnode = KV.insert_prim(atnode, k, gen_val(k))
        assert flag, str_form(test_objective, False, True, reason + ': sequential insertion into tree failed')

    for v in [6, 19, 0, 44]:
        retflag, retval = KV.delete_prim(atnode, v)
        expected = False
        assert retflag == expected, str_form(test_objective, retflag, expected,
                                             reason + ': unexpected deletion for key' + str(k))


def test_25():
    test_objective = 'insert_prim() + delete_prim()'
    reason = 'voluminous tree, all keys, delete values sequentially'

    keys = [5, 3, 1, 8, 10, 7, 2]

    # create a tree from scratch with all the keys
    atnode = None
    for k2 in keys:
        flag, atnode = KV.insert_prim(atnode, k2, gen_val(k2))
        assert flag, str_form(test_objective, False, True, reason + ': sequential insertion into tree failed')

    deleted = []
    for k in keys:
        # remove just the one key k
        retflag, retval = KV.delete_prim(atnode, k)
        expected = True
        assert retflag == expected, str_form(test_objective, retflag, expected,
                                             reason + ': failed to find key ' + str(k))
        deleted.append(k)

        # check that the others are all still there
        for v in keys:
            if v not in deleted:
                retflag, retval = KV.member_prim(atnode, v)
                expected = True
                assert retflag == expected, str_form(test_objective, retflag, expected,
                                                     reason + ': failed to find key ' + str(k))
                expected = gen_val(v)
                assert retval == expected, str_form(test_objective, retval, expected,
                                                    reason + ': failed to find data value')
