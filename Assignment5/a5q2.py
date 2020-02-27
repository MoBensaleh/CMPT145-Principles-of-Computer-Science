# CMPT 145: Assignment 5 Question 2
# Mohamed Bensaleh
# Mob127
# 11254030

import node as node



def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """

    if node_chain == None:
        return 0
    else:
        return 1 + count_chain(node.get_next(node_chain))


def delete_front_nodes(node_chain, n):
    """
    Purpose:
        Deletes the first n nodes from the front of the node chain.
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param n: integer, how many nodes that should be removed off the front of the node chain
    Post-conditions:
        The node-chain is changed, by removing the first n nodes. If n>length of node_chain, node_chain is set to be empty (None)
    Return:
        :return: The resulting node chain, which may now be empty (None)
    """
    if n <= 0:
        return node_chain
    if node_chain == None:
        return None
    else:
        return delete_front_nodes(node.get_next(node_chain), n - 1)


def replace_last(node_chain, target_val, replacement_val):
    """
    Purpose:
        Replaces the last occurrence of target data value with the new_value. The chain should at most have 1 data value changed.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
        :param target_val: the target data value we are searching to replace the last instance of
        :param replacement_val: the data value to replace the target_val that we found
    Post-conditions:
        The node-chain is changed, by replacing the last occurrence of target_val. If target_val is not present, then the node_chain returns unaltered.
    Return:
        :return: The altered node chain where any data occurrences of target_val has been replaced with replacement_val.
    """
    n = None
    start = node_chain
    while start != None:
        if(node.get_data(start) == target_val):
            n = start
        start = node.get_next(start)

    if n != None:
        node.set_data(n, replacement_val)

    return node_chain