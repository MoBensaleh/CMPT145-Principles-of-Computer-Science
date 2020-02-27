# CMPT 145: Binary trees
# defines a few convenience functions that allow us to test functions on primitive trees
# For functions that return primitive trees as created by treenode.create(), we don't want to
# build dictionaries for our tests.

import treenode as tn
import TQueue as Queue

def in_to_string(tnode):
    """
    Purpose:
        Return a string representing a primitive binary tree.  
        The string is composed of the data values of the tree,
        ordered by the in-order traversal.
    Pre-conditions:
        :param tnode: a primitive tree
    Post-conditions:
        The tree is unaffected
    Return
        :return: a string representation
    """
    if tnode is None:
        return ""
    else:
        leftbits  = in_to_string(tn.get_left(tnode))
        rightbits = in_to_string(tn.get_right(tnode))
        return leftbits + str(tn.get_data(tnode)) + ' ' + rightbits




def breadth_first_to_string(tnode):
    """
    Purpose:
        Return a string representing a primitive binary tree.  
        The string is composed of the data values of the tree,
        ordered by the breadth-first order traversal.
    Pre-conditions:
        :param tnode: a primitive tree
    Post-conditions:
        The tree is unaffected
    Return
        :return: a string representation
    """
    # the nodes queue keeps track of which nodes to look at
    nodes = Queue.create()
    Queue.enqueue(nodes, tnode)
    
    # the order queue stores the data values of the nodes we've looked at
    order = Queue.create()

    while Queue.size(nodes) > 0:
        current = Queue.dequeue(nodes)
        if current is not None:
            Queue.enqueue(order, tn.get_data(current))
            Queue.enqueue(nodes, tn.get_left(current))
            Queue.enqueue(nodes, tn.get_right(current))

    # produce a string of the data values from the order queue
    result = ''
    while not Queue.is_empty(order):
        n = Queue.dequeue(order)
        result = result + str(n) + ' '

    return result



def to_string_for_testing(tnode):
    """ 
    Purpose:    
        Create a complex string that uniquely identifies a tree.
        The combination of inorder nodes and breadth-first nodes uniquely identifies
        a tree structure, assuming the data values are not repeated.
    Pre-conditions:
        :param tnode: a primitive tree
    Post-conditions:
        The tree is unaffected
    Return
        :return: a string representation
    """
    return in_to_string(tnode) + '. ' + breadth_first_to_string(tnode)



def to_string_for_printing(tnode, level=0):
    """
    Purpose:
        Produce a formatted string to represent the hierarchy of
        a tree.  Tree diagrams usually have the root at the top.
        Here the root is at the top left.
        - every data value appears on its own line
         - the levels of a tree are columns from left to right
        - nodes at the same level start in the same column
        - very long data values might cause the presentation to get messy
        - subtrees appear below a parent, indented by a tab
            - left subtree immediately
            - right subtree after the entire left subtree
            - the level determines the number of tabs for indentation
    Pre-conditions:
        :param tnode: a primitive binary tree (treenode or None)
        :param level: the level of the tnode (default value 0)
    Return:
        A string with the hierarchy of the tree, that can be printed.
    """
    if tnode is None:
        return 'EMPTY'
    else:
        result = '\t'*level
        result += str(tn.get_data(tnode))
        if tn.get_left(tnode) is not None:
            result += '\n'+to_string_for_printing(tn.get_left(tnode), level+1)
        if tn.get_right(tnode) is not None:
            result += '\n'+to_string_for_printing(tn.get_right(tnode), level+1)
        return result
