# CMPT 145: Binary trees

# This file is copyright (c) Michael C Horsch, provided solely for the
# use of CMPT 145 students.  Students are welcome to use this file
# for their own work, and make copies for their own personal use.
# This file should not be shared for any reason without explicit
# consent of the author.

# Defines the kv tree node ADT
#
# A KVTreeNode is a simple container with four pieces of
# information:
#   key:   the key for the node, used to organize the tree
#   value: the contained information
#   left:  a reference to another KVTreeNode, or None
#   right: a reference to another KVTreeNode, or None


# Implementation notes:
#    This is an  ADT, using objects instead of dictionaries
#    Attributes are public for convenience

class KVTreeNode(object):
    def __init__(self, key, value, left=None, right=None):
        """
        Purpose:
            Create a new KVTreeNode for the given data.
        Pre-conditions:
            key:    A key used to identify the node
            value:  Any data value to be stored in the KVTreeNode
            left:   Another KVTreeNode (or None, by default)
            right:  Another KVTreeNode (or None, by default)
        """
        self.value = value
        self.left = left
        self.right = right
        self.key = key

