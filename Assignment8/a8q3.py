# Mohamed Bensaleh
# CMPT 145 Assignment 8
# Mob127
# 11254030

import treenode as tn

def bad_complete(tnode):
    def complete(tnode):
        if tnode is None:
            return 0
        else:
            ldepth = complete(tn.get_left(tnode))
            rdepth = complete(tn.get_right(tnode))
            if ldepth == rdepth:
                return rdepth+1
            else:
                return -1
    result = complete(tnode)
    return result > 0



def complete(tnode):
    """
 Purpose:
     A tree is complete if all nodes have 2 non-empty
     subtrees, except for the nodes at maximum level,
     which are all leaf nodes.
 Pre-conditions:
     :param tnode: a tree node
Post-Conditions:
    None
 Return
     :return: True if the tree is complete, False otherwise.
 """
    """
    :return: (True, height) if tnode is complete
             (False, None) is tnode is not complete
    """
    if tnode is None:
        return True, 0
    else:
        lflag, ldepth = complete(tn.get_left(tnode))
        if not lflag:
            return False, None
        rflag, rdepth = complete(tn.get_right(tnode))
        if not rflag:
            return False, None
        if ldepth == rdepth:
            return True, rdepth + 1
        else:
            return False, None

    result, _ = complete(tnode)
    return result
