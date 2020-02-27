# CMPT 145: Primitive Binary Search Trees

# This file is copyright (c) Michael C Horsch, provided solely for the
# use of CMPT 145 students.  Students are welcome to use this file
# for their own work, and make copies for their own personal use.
# This file should not be shared for any reason without explicit
# consent of the author.


# Defines functions for primitive Binary Search Tree data structure
#
# A Primitive Binary Tree is defined as follows:
# 1. The value None is a primitive binary tree;
#    (None represents an empty tree)
# 2. If lt and rt are primitive binary trees, and d is any value
#    TreeNode(d, lt, rt) is a primitive binary tree.
#
# A TreeNode is analogous to a Node in a node-chain. 
# 
# A Primitive Binary Tree t satisfies the Binary Search Tree (BST)
# property if all of the following hold:
# 0. If t is None, it satisfies the BST property by definition.
#    Otherwise, we assume t is a TreeNode object
# 1. The data value stored at TreeNode t is greater than any data
#    value in t's left subtree (if any)
# 2. The data value stored at TreeNode t is smaller than any data
#    value in t's right subtree (if any)
# 3. t's left subtree satisfies the BST property
# 4. t's right subtree satisfies the BST property


import TreeNode as tn


def member_prim(tnode, target):
    """
    Purpose:
        Check if target is stored in the binary search tree.
    Pre-Conditions:
        :param tnode: a TreeNode with the BST property
        :param target: a value
    Post -Conditions:
        none
    Return
        :return: True if target is in the tree
    """

    if tnode is None:
        return False
    elif tnode.data is target:
            return True
    elif target > tnode.data:
        return member_prim(tnode.left, target)
    else:
        return member_prim(tnode.left, target)



def insert_prim(tnode, value):
    """
    Insert a new value into the binary search tree.
    Pre-Conditions:
        :param tnode: a TreeNode with the BST property
        :param value: a value
    Post -Conditions:
        If the value is not already in the tree, it is added
    Return
        :return: tuple (flag, tree)
            flag is True if insertion succeeded;
                    tree contains the new value
            flag is False if the value is already in the tree,
                    tree unchanged
    """

    if tnode is None:
        return True, tn.TreeNode(value)
    else:
        if tnode.data is value:
            return False, tnode
        elif value < tnode.data:
            left, left_val = insert_prim(tnode.left, value)
            if left_val:
                tnode.left = left
                return True, tnode
            return True, tnode
        else:
            right, right_val = insert_prim(tnode.right, value)
            if right:
                tnode.right = right_val
                return True, tnode
            return True, tnode


def delete_prim(tnode, target):
    """
    Delete a target from the binary search tree.
    Pre-Conditions:
        :param tnode: a TreeNode with the BST property
        :param target: a value
    Post -Conditions:
        If the target is in the tree, it is deleted.
        If the target is not there, there is no change to the tree.
    Return
        :return: tuple (flag, tree)
           -flag is True if deletion succeeded;
            tree is the resulting without the value
           -flag is False if the value was not in the tree,
            tree returned unchanged
    """

    def delete(tnode):
        '''Internal function does most of the deleting work'''
        if tnode is None:
            return False, tnode
        else:
            cval = tnode.data
            if cval == target:
                return reconnect(tnode)
            elif target < cval:
                flag, subtree = delete(tnode.left)
                if flag:
                    tnode.left = subtree
                return flag, tnode
            else:
                flag, subtree = delete(tnode.right)
                if flag:
                    tnode.right = subtree
                return flag, tnode

    def reconnect(delthisnode):
        '''
            Reconnect the tree by removing delthisnode.
            Internal function implements the 4 cases.
        '''
        if delthisnode.left is None and delthisnode.right is None:
            # Case 1: delthisnode has no children
            return True, None

        elif delthisnode.left is None:
            # Case 2: delthisnode has a right child only
            return True, delthisnode.right

        elif delthisnode.left is None:
            # Case 3: the deleted node has a left child only
            return True, delthisnode.left

        else:
            # Case 4: delthisnode has two children

            # every value in oldright is bigger than any value in oldleft
            oldleft = delthisnode.left
            oldright = delthisnode.right

            # find the place in oldleft to attach oldright
            # at the bottom right of oldleft!
            walker = oldleft
            while walker.right is not None:
                walker = walker.right

            # attach
            walker.right = oldright

            # oldleft has all the values, and is the new tree
            return True, oldleft

    # the body of delete_prim() is very short:
    return delete(tnode)

