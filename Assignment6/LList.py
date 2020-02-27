# Mohamed Bensaleh
# CMPT 145
# 11254030
#

# CMPT 145: Node-Based Data Structures
# Defines the Linked List ADT
#
# Here we re-invent Python's built-in lists.  We will provide a subset of
# the operations that a Python list provides.
#
# Implementation:
#   This implementation uses the linked node structure.

import node as node


def create():
    """
    Purpose
        creates an empty list
    Return
        :return an empty list
    """
    llist = {}
    llist['size'] = 0     # how many elements in the stack
    llist['head'] = None  # the node chain starts here; initially empty
    llist['tail'] = None
    return llist



def is_empty(alist):
    """
    Purpose
        Checks if the given list has no data in it
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return True if the list has no data, or False otherwise
    """
    if (alist['size'] == 0):
        return True
    return False



def size(alist):
    """
    Purpose
        Returns the number of data values in the given list
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return The number of data values in the list
    """
    return alist['size']



def add_to_front(alist, val):
    """
    Purpose
        Insert val into alist at the front of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is at index 0.
        The values previously in the list appear after the new value.
    Return:
        :return None
    """
    newNode = node.create(val, alist['head'])
    alist['head'] = newNode
    if alist['tail'] == None:
        alist['tail'] = newNode
    alist['size'] += 1
    return alist



def add_to_back(alist, val):
    """
    Purpose
        Insert val into alist at the end of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is last in the list.
    Return:
        :return None
    """
    newNode = node.create(val, None)
    if size(alist) == 0:
        alist['head'] = newNode
        alist['tail'] = newNode
    else:
        node.set_next(alist['tail'], newNode)
        alist['tail'] = newNode
    alist['size'] += 1  # incrementing size
    return alist



def value_is_in(alist, val):
    """
    Purpose
        Check if the given value is in the given list
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return True if the value is in the list, False otherwise
    """
    nod = alist['head']
    while nod is not None:
        if node.get_data(nod) == val:
            return True
        nod = node.get_next(nod)
    return False


def get_index_of_value(alist, val):
    """
    Purpose
        Return the smallest index of the given val in the given alist.
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return the tuple (True, idx) if the val appears in alist
        :return the tuple (False, None) if the vale does not appear in alist
    """
    if alist == None:
        return (False, None)
    idx = 0
    nod = alist['head']
    while nod != None:
        if node.get_data(nod) == val:
            return (True, idx)
        nod = node.get_next(nod)
        idx += 1
    return (False, None)



def retrieve_data_at_index(alist, idx):
    """
    Purpose
        Return the value stored in alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        none
    Return:
        :return (True, val) if val is stored at index idx and idx is valid
        :return (False, None) if the idx is not valid for the list
    """
    if alist == None:
        return (False, None)
    index = 0
    nod = alist['head']
    while nod != None:
        if index == idx:
            return (True, node.get_data(nod))
        nod = node.get_next(nod)
        index += 1
    return (False, None)



def set_data_at_index(alist, idx, val):
    """
    Purpose
        Store val into alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a non-negative integer
    Post-conditions:
        The value stored at index idx changes to val
    Return:
        :return True if the index was valid, False otherwise
    """
    if alist == None:
        return False
    index = 0
    nod = alist['head']
    while nod != None:
        if index == idx:
            node.set_data(nod, val)
            return True
        nod = node.get_next(nod)
        index += 1
    return False



def remove_from_front(alist):
    """
    Purpose
        Removes and returns the first value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    if alist['size'] != 0:
        value = node.get_data(alist['head'])
        alist['head'] = node.get_next(alist['head'])
        alist['size'] -= 1
        if alist['head'] == None:
            alist['tail'] = None
        return True, value
    return False, None



def remove_from_back(alist):
    """
    Purpose
        Removes and returns the last value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    if alist['size'] != 0:
        nod = alist['head']
        nxtnod = node.get_next(nod)
        if nxtnod == None:
            # removing the head element in the list
            value = node.get_data(nod)
            alist['head'] = None
            alist['tail'] = None
            alist['size'] = 0
            return True, value
        # looping until nxtnod is equal to tail node
        while nxtnod != alist['tail']:
            nod = nxtnod
            nxtnod = node.get_next(nxtnod)
        # getting data of tail node
        value = node.get_data(alist['tail'])
        # deleting the tail node and updating it with previous node
        node.set_next(nod, None)
        alist['tail'] = nod
        alist['size'] -= 1
        return True, value
    return False, None


def insert_value_at_index(alist, val, idx):
    """
    Purpose
        Insert val into alist at index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a valid index for the list
    Post-conditions:
        The list increases in size.
        The new value is at index idx.
        The values previously in the list at idx or later appear after the new value.
    Return:
        :return If the index is valid, insert_value_at_index returns True.
        :return If the index is not valid, insert_value_at_index returns False.
    """
    if idx >= 0 and idx <= alist['size']:
        if idx == 0:
            # inserting at the front
            add_to_front(alist, val)
            return True
        if idx == alist['size']:
            # inserting at the back
            add_to_back(alist, val)
            return True
        i = 0
        nod = alist['head']
        while i < idx - 1:
            nod = node.get_next(nod)
            i += 1
        # inserting between two nodes
        newnode = node.create(val, node.get_next(nod))
        node.set_next(nod, newnode)
        alist['size'] += 1
        return True
    return False



def delete_item_at_index(alist, idx):
    """
    Purpose
        Delete the value at index idx in alist.
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        The list decreases in size if the index is valid
        The value at idx is no longer in the list.
    Return:
        :return True if index was valid, False otherwise
    """
    if idx >= 0 and idx < alist['size']:
        if idx == 0:
            # removing from front
            remove_from_front(alist)
            return True
        if idx == alist['size'] - 1:
            # removing from back
            remove_from_back(alist)
            return True
        i = 0
        nod = alist['head']
        # finding the node at specified index
        while i < idx - 1:
            nod = node.get_next(nod)
            i += 1
        # removing from the middle of two nodes
        nextnode = node.get_next(nod)
        nextnode = node.get_next(nextnode)
        node.set_next(nod, nextnode)
        alist['size'] -= 1
        return True
    return False




