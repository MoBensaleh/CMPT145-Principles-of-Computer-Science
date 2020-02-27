class Node(object):
    def __init__(self, value, next_node=None):
        self.__data = value      # Private!
        self.__next = next_node      # Private!

    def get_data(self):
        """
        Purpose:
            returns the data stored in the node
        Pre-conditions:
            None
        Post-condition:
            None
        Return:
            returns the data stored in the node, or None if it is empty
        """
        return self.__data

    def get_next(self):
        """
        Purpose:
            returns the node stored the next field
        Pre-conditions:
            None
        Post-condition:
            None
        Return:
            returns the node stored in the next field, or None if it is empty
        """
        return self.__next

    def set_data(self, value):
        """
        Purpose:
            sets the data of node to be value
        Pre-conditions:
            None
        Post-condition:
            Node now contains the data value
        Return:
            None
        """
        self.__data = value

    def set_next(self, next_node):
        """
        Purpose:
            sets the next field to point to the node next_node
        Pre-conditions:
            None
        Post-condition:
            the next field now points to next_node
        Return:
            None
        """
        self.__next = next_node
