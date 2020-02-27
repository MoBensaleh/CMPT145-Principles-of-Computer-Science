# CMPT 145: Object Oriented Programming
# 201901 Assignment 9 Questions 1, 2


# to use this file for Q2, change the import line below
import a9q1_Stack as Stack


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
    return ' '.join(['Test fault:',obj,
                     'returned',str(result),
                     '(expected:', str(exp)+')',
                     'on:',reason])


def test_0():
    astack = Stack.Stack()
    assert isinstance(astack, Stack.Stack), 'Test fault: __init__ failed'


def test_1():
    test_objective = 'is_empty()'
    reason = 'empty stack'
    astack = Stack.Stack()
    result = astack.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_2():
    test_objective = 'size()'
    reason = 'empty stack'
    astack = Stack.Stack()
    result = astack.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_3():
    test_objective = 'is_empty()'
    reason = 'stack with one value'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_4():
    test_objective = 'size()'
    reason = 'stack with one value'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_5():
    test_objective = 'peek()'
    reason = 'pushed 1'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.peek()
    expected = 'value'
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_6():
    test_objective = 'size()'
    reason = 'pushed 1 then peeked'
    astack = Stack.Stack()
    astack.push('value')
    ignore = astack.peek()
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_7():
    test_objective = 'isempty()'
    reason = 'pushed 1 then peeked'
    astack = Stack.Stack()
    astack.push('value')
    ignore = astack.peek()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_8():
    test_objective = 'pop()'
    reason = 'pushed 1 then popped 1'
    astack = Stack.Stack()
    astack.push('value')
    result = astack.pop()
    expected = 'value'
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_9():
    test_objective = 'is_empty()'
    reason = 'pushed 1 then popped 1'
    astack = Stack.Stack()
    astack.push('value')
    temp = astack.pop()
    result = astack.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_10():
    test_objective = 'size()'
    reason = 'pushed 1 then popped 1'
    astack = Stack.Stack()
    astack.push('value')
    temp = astack.pop()
    result = astack.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_11():
    test_objective = 'size()'
    reason = 'pushed 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.size()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_12():
    test_objective = 'is_empty()'
    reason = 'pushed 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_13():
    test_objective = 'peek()'
    reason = 'pushed 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.peek()
    expected = 'second'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_14():
    test_objective = 'size()'
    reason = 'pushed 2 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.peek()
    result = astack.size()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_15():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.peek()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_16():
    test_objective = 'pop()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    result = astack.pop()
    expected = 'second'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_17():
    test_objective = 'size()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_18():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_19():
    test_objective = 'peek()'
    reason = 'pushed 2 then popped 1'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.pop()
    result = astack.peek()
    expected = 'first'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_20():
    test_objective = 'size()'
    reason = 'pushed 2 then popped 1 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.pop()
    ignore = astack.peek()
    result = astack.size()
    expected = 1
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_21():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then popped 1 then peeked'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    ignore = astack.pop()
    ignore = astack.peek()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_22():
    test_objective = 'is_empty()'
    reason = 'pushed 2 then popped 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    temp = astack.pop()
    result = astack.is_empty()
    expected = True
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_23():
    test_objective = 'size()'
    reason = 'pushed 2 then popped 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    temp = astack.pop()
    result = astack.size()
    expected = 0
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_24():
    test_objective = 'pop()'
    reason = 'pushed 2 then popped 2'
    astack = Stack.Stack()
    astack.push('first')
    astack.push('second')
    temp = astack.pop()
    result = astack.pop()
    expected = 'first'
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_25():
    test_objective = 'size()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.size()
    expected = 10
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_26():
    test_objective = 'is_empty()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)

def test_27():
    test_objective = 'peek()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.peek()
    expected = 9
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_28():
    test_objective = 'pop()'
    reason = 'pushed 10'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    result = astack.pop()
    expected = 9
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_29():
    test_objective = 'is_empty()'
    reason = 'pushed 10 popped 1'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    ignore = astack.pop()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_30():
    test_objective = 'size()'
    reason = 'pushed 10 popped 1'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    ignore = astack.pop()
    result = astack.size()
    expected = 9
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_31():
    test_objective = 'peek()'
    reason = 'pushed 10 popped 1'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    ignore = astack.pop()
    result = astack.peek()
    expected = 8
    assert result == expected, str_form(test_objective, result, expected, reason)



def test_32():
    test_objective = 'is_empty()'
    reason = 'pushed 10 popped 7'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    for i in range(7):
        ignore = astack.pop()
    result = astack.is_empty()
    expected = False
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_33():
    test_objective = 'size()'
    reason = 'pushed 10 popped 7'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    for i in range(7):
        ignore = astack.pop()
    result = astack.size()
    expected = 3
    assert result == expected, str_form(test_objective, result, expected, reason)


def test_34():
    test_objective = 'peek()'
    reason = 'pushed 10 popped 7'
    stuff = list(range(10))
    astack = Stack.Stack()
    for st in stuff:
        astack.push(st)
    for i in range(7):
        ignore = astack.pop()
    result = astack.peek()
    expected = 2
    assert result == expected, str_form(test_objective, result, expected, reason)

