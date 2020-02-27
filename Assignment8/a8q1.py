# Mohamed Bensaleh
# CMPT 145 Assignment 8
# 11254030
# Mob127

from treenode import *


def count_node_types(tnode):
    '''
    Purpose: calculates and returns a tuple containing the number of leaf nodes in the tree,
and the number of non-leaf nodes in the tree.
    Pre-Conditions:
        :param tnode: A tree node
    Post-Conditions: none
    :return: Returns a tuple containing the number of leaf nodes in the tree,
and the number of non-leaf nodes in the tree
    '''
    if(tnode==None):
        return (0,0)
    elif get_left(tnode) is None and get_right(tnode) is None:
        return (1,0)
    else:
        left = count_node_types(tnode['left'])
        right = count_node_types(tnode['right'])
    return (left[0]+right[0],left[1]+right[1]+1)


def subst(tnode, t, r):
    '''
    Purpose: Substitutes a target value t with a replacement value r wherever it appears as a data value in the given tree.
    Pre-Conditions:
        :param tnode: A tree node
        :param t: target value
        :param r: replacement value
    Post-Conditions: modifies the tree by replacing every target value with the replacement value
    :return: None
    '''
    if tnode is None:
        return None
    if get_data(tnode) == t:
        set_data(tnode, r)
        subst(get_left(tnode), t, r)
        subst(get_right(tnode), t, r)


def copy(tnode):
    '''
    Purpose: To create an exact copy of the given tree, with completely new treenodes, but exactly the same data values,
     in exactly the same places.
    Pre-Conditions:
        :param tnode: A tree node
    Post Conditions: none
    :return: If tnode is None, return None. If tnode is not None, return a reference to the new tree.
    '''
    if tnode is None:
        return None
    return create(data=get_data(tnode),
    left=copy(get_left(tnode))
    , right=copy(get_right(tnode)))


# assuming level starts from 0
def nodes_at_level(tnode,level):
    '''
    Purpose: Counts the number of nodes in the given primitive tree at the given level
    Pre-Conditions:
        :param tnode: A tree node
        :param level: the given level to be counted
    Post-Conditions: none
    :return: returns the count of nodes at the given level
    '''
    if(tnode==None):
        return 0
    elif(level<0):
        return 0
    elif(level==0):
        return 1
    return nodes_at_level(tnode['left'],level-1)+nodes_at_level(tnode['right'],level-1)

