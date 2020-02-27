# Mohamed Bensaleh
# CMPT 145 Assignment 8
# 11254030
# Mob127

import treenode as tn


def mirrored(t1, t2):
    """
    Purpose
            To find if two trees have exact same structure and value
    Pre-conditions:
            t1 and t2 are valid trees created by create()
    Return:
            True if both have same data and alignment, else False
    """
    # if both tree empty
    if t1 is None and t2 is None:
        return True

    # if any one tree is empty
    if t1 is None or t2 is None:
        return False

    # check data on both nodes.
    if tn.get_data(t1) != tn.get_data(t2):
        return False

    # check for subtrees to satisfy mirror property
    return mirrored(tn.get_left(t1), tn.get_right(t2)) and mirrored(tn.get_right(t1), tn.get_left(t2))



def reflect(tnode):
    """
    Purpose
            To swap the left and right children in memory for all nodes of tree
    Pre-conditions:
            tnode is a valid tree created by create()
    Post-conditions:
            modifies the given tree by swapping every left and right subtree in the given primitive tree
    Return:
            None
    """
    if tnode is None:
        return None

    # swap left and right pointer data on node
    l = tn.get_left(tnode)
    r = tn.get_right(tnode)

    tn.set_left(tnode, r)
    tn.set_right(tnode, l)

    # call recursively
    reflect(l)
    reflect(r)



def reflection(tnode):
    """
    Purpose
            To create a new tree with left and right child swapped
    Pre-conditions:
            tnode is a valid tree created by create()
    Post-conditions:
            none
    Return:
            A new tree is returned which is the mirror copy of input tree
    """
    if tnode is None:
        return None

    # create a new node for current node, and attach reflected left and right
    # children to it.
    return tn.create(tn.get_data(tnode), reflection(tn.get_right(tnode)), reflection(tn.get_left(tnode)))