# Mohamed Bensaleh
# CMPT 145 Assignment 9
# Mob127
# 11254030


from Node import Node


class Container:

    def __init__(self):
        """
        Purpose
                Constructor: creates an empty container
        Post-condition:
                container is created with no values inside
        Return
                None
        """
        self.__front = None #front of container
        self.__back=None #back of container
        self.__size = 0

    def size(self):
        """
        Purpose
                returns the number of data values in the container
        Post-condition:
                None
        Return:
                The number of data values in the container
        """
        return self.__size

    def is_empty(self):
        """
        Purpose
                checks if the container has no data in it
        Post-condition:
                None
        Return:
                True if the container has no data, or false otherwise
        """
        return self.__size == 0

    def removeFront(self):
        """
        Purpose
                removes and returns the front value from the current container
        Post-condition:
                the first value is removed from the container
        Return:
                the first value in the container, or None
        """
        assert not self.is_empty()

        result = self.__front
        self.__front = self.__front.get_next()
        if self.__front==None:
            self.__back=None
        self.__size -= 1
        return result.get_data()

    def insertFront(self, value):
        """
        Purpose
                adds the given data value to the front of the container
        Pre-conditions:
                value: data to be added
        Post-condition:
                the value is added to the container
        Return:
                (none)
        """
        self.__front = Node(value, self.__front)
        if self.__back==None:
            self.__back=self.__front
        self.__size += 1

    def insertRear(self, value):
        """
        Purpose
                adds the given data value to the back of the container
        Pre-conditions:
                value: data to be added
        Post-condition:
                the value is added to the back of container
        Return:
                (none)
        """
        # create a new node with value
        new_node = Node(value)

        # if container is initially empty.
        if self.__size == 0:
            self.__front = new_node
        else:
            # set the new node as the last node
            self.__back.set_next(new_node)

        # update the last node and size of queue
        self.__back = new_node
        self.__size += 1


    def front(self):
        """
        Purpose
                returns the value from the front of container
                without removing it
        Post-condition:
                None
        Return:
                the value at the front of the container
        """
        assert not self.is_empty()
        return self.__front.get_data()

    def rear(self):
        """
        Purpose
                returns the rear value from the container
                without removing it
        Post-condition:
                None
        Return:
                the value at the front of the container
        """
        assert not self.is_empty()
        return self.__back.get_data()

    def to_string(self):
        """
        Purpose:
                Create a string representation of the Stack. E.g.,
                [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
                where 1 is the top of the container and 3 is the end of the container
        Post_conditions:
                None
        Return: A string representation of the container.
        """
        # special case: empty container
        if self.is_empty():
            result = 'EMPTY'
        else:
            # walk along the chain
            walker = self.__front

            value = walker.get_data()
            result = '[ ' + str(value) + ' |'

            while walker.get_next() is not None:
                walker = walker.get_next()

                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'

            # at the end of the container, use '/'
            result += ' / ]'

        return result

