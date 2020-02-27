# CMPT 145: Assignment 5 Question 3
# Mohamed Bensaleh
# Mob127
# 11254030

import node as node
import a5q2 as a5q2
import a5q1 as a5q1


def contains_duplicates(node_chain):
    """
    Purpose:
        Returns whether or not the given node_chain contains one or more duplicate data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Return:
        :return: True if duplicate data value(s) were found, False otherwise
    """
    if a5q2.count_chain(node_chain) == 0:
        # empty chain
        return False
    nodes_list = []
    # getting first node in the chain
    start = node_chain
    # looping until the node is empty
    while start != None:
        data = node.get_data(start)
        if data in nodes_list:
            return True
        nodes_list.append(data)
        # getting next node
        start = node.get_next(start)
    # if the while loop successfully complete without returning anything, it means that there is no duplicates
    return False


# testing the above function

chain = node.create(1,
        node.create(2,
        node.create(3,
        node.create(4,
        node.create(5)))))

print('Duplicates?', contains_duplicates(chain))
altered_chain = a5q2.replace_last(chain, 5, 1)
print('Duplicates?', contains_duplicates(altered_chain))


def reverse_chain(node_chain):
    """
    Purpose:
        Completely reverses the order of the given node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Post-conditions:
        The front of the node_chain is altered to be the back, with all nodes now pointing next the opposite direction.
    Return:
        :return: The resulting node chain that has had its order reversed
    """
    if a5q2.count_chain(node_chain) <= 1:
        return node_chain
    data_list = []
    start = node_chain
    # iterating through all nodes
    while start != None:
        # appending the node's data to the list
        data_list.append(node.get_data(start))
        start = node.get_next(start)
    start = node_chain
    # finding the last index of the list
    index = len(data_list) - 1
    # iterating once more through the list, from the beginning
    while start != None:
        # setting data at the list's 'index' position as data of current node (reverse order)
        node.set_data(start, data_list[index])
        start = node.get_next(start)  # next node
        index -= 1  # previous index
    return node_chain


# demonstrating reverse_chain method

chain = node.create(1, node.create('two', node.create(3)))
print('before:', a5q1.to_string(chain))
reversed_chain = reverse_chain(chain)
print('after:', a5q1.to_string(chain))


def insert_value_sorted(node_chain, number_value):
    """
    Purpose:
        Insert the given number_value into the node-chain so that it appears after a previous value that is <= value. If the node_chain was empty, new value is simply placed at the front.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing only numbers
        :param number_value: a numerical value to be inserted
        Assumption:  node_chain only contains numbers (which can be compared to the given number_value)
    Post-condition:
        The node-chain is modified to include a new node with number_value as its data after a previous node's data value is <= number_value.
    Return
        :return: the node-chain with the new value in it
    """
    start = node_chain
    if start == None:
        # first value
        start = node.create(number_value)
        return start

    nextnode = node.get_next(start)  # next node
    if nextnode == None:  # no second node
        # adding to first or second position based on value
        if node.get_data(start) <= number_value:
            node_ = node.create(number_value)
            node.set_next(start, node_)
            return start
        else:
            start = node.create(number_value, start)
            return start

    if number_value <= node.get_data(start):
        # adding to first position when there are more than two nodes
        node_ = node.create(number_value, start)
        return node_
    # looping through all nodes
    while nextnode != None:
        # checking if data can be added in the middle
        if number_value >= node.get_data(start) and number_value < node.get_data(nextnode):
            node_ = node.create(number_value, nextnode)
            node.set_next(start, node_)
            return node_chain

        start = node.get_next(start)
        nextnode = node.get_next(nextnode)

    # appending to the end
    node_ = node.create(number_value)
    node.set_next(start, node_)
    return node_chain


# demonstrating the insert_value_sorted method
chain = node.create(1, node.create(2, node.create(4, node.create(5))))
print('before:', a5q1.to_string(chain))
chain = insert_value_sorted(chain, 3)
print('after:', a5q1.to_string(chain))


