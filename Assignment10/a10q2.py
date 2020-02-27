# Mohamed Bensaleh
# CMPT 145 Assignment 10
# Mob127
# 11254030


# CMPT 145:  Binary Search Trees

# This file is copyright (c) Michael C Horsch, provided solely for the
# use of CMPT 145 students.  Students are welcome to use this file
# for their own work, and make copies for their own personal use.
# This file should not be shared for any reason without explicit
# consent of the author.

# Implements the Table ADT
#
# Data structure:
#   a table is a object containing two attributes:
#     __root  - value stores the root of a primitive binary tree
#     __size  - value stores the number of nodes in the primitive binary tree
# The methods ensure that the primitive binary tree satisfies the
# binary search tree property

import a10q1 as bst

class Table(object):
    def __init__(self):
        self.__root = None
        self.__size = 0


    def size(self):
        """
        Purpose:
            Return the size of the table.
        Post_condition:
            The Table does not change
        Return:
            :return: the number of key,value pairs in the Table
        """
        return self.__size


    def is_empty(self):
        """
        Purpose:
            Indicate whether the given table is empty.
        Post_condition:
            The Table does not change
        Return:
            :return: True if the table is empty
        """
        return self.__size==0

    def retrieve(self, key):
        """
        Purpose:
          Return the value associated with the given key.
        Preconditions:
            :param key: a key
        Post-condition:
            The Table does not change
        Return
            :return: True, value if the key appears in the table
                     False, None otherwise
        """
        #using member_prim() method to check if there is a key exists in self.__root tree
        return bst.member_prim(self.__root,key)

    def insert(self, key, value):
        """
        Purpose:
          Insert a new key, value into the table.
        Preconditions:
            :param key: a unique key for the value
            :param value: a value
        Post-condition:
            If the key is not already in the table, it is added to the table
            If the key is already in the table, change the value (not the key)
        Return
            :return: True if the key,value was inserted
                     False if the value of an existing key was changed
        """
        #using insert_prim() method to add a key value pair to self.__root tree
        result,self.__root=bst.insert_prim(self.__root,key,value)
        if result:
            #addition success, updating size
            self.__size+=1
        #returning the result
        return result

    def delete(self, key):
        """
        Purpose:
            Delete a given key and its associated value from the table.
        Preconditions:
            :param key: a unique key
        Postconditions:
            If the key is not in the table, no change to the table
            If the key is in the table, remove it and the associated value
        Return
            :return: True if the key,value was deleted
                     False otherwise
        """
        # using delete_prim() method to delete a key value pair from self.__root tree
        # if exists.
        result,self.__root=bst.delete_prim(self.__root,key)
        if result:
            #removal success, updating size
            self.__size-=1
        return result


    def in_order(self):
        """
        Purpose:
            Returns a string of the keys showing the in-order sequence.
            May be useful for testing and debugging.
        Return:
            A string representing the state of the Table
        """

        def in_order_prim(kvtnode):

            if kvtnode is None:
                return " "
            else:
                before = in_order_prim(kvtnode.left)
                this = '('+str(kvtnode.key)+','+str(kvtnode.value)+')'
                after = in_order_prim(kvtnode.right)
                return before + this + after

        return in_order_prim(self.__root)