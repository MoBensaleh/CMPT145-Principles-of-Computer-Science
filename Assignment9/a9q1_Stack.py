# Mohamed Bensaleh
# CMPT 145 Assignment 9
# Mob127
# 11254030


from Node import Node


class Stack:
    '''
    Stack class represent a Last In First Out structure.
    This has common methods such as to push the data, pop
    the values, find size and check if stack is empty.
    '''

    def __init__(self):
        """
        Purpose
                Constructor: creates an empty stack
        Post-condition:
                Stack is created with no values inside
        Return
                None
        """
        self.__top = None
        self.__size = 0

    def size(self):
        """
        Purpose
                returns the number of data values in the stack
        Post-condition:
                None
        Return:
                The number of data values in the stack
        """
        return self.__size

    def is_empty(self):
        """
        Purpose
                checks if the stack has no data in it
        Post-condition:
                None
        Return:
                True if the stack has no data, or false otherwise
        """
        return self.__size == 0

    def pop(self):
        """
        Purpose
                removes and returns a data value from the current stack
        Post-condition:
                the first value is removed from the stack
        Return:
                the first value in the stack, or None
        """
        assert not self.is_empty(), 'popped an empty stack'

        result = self.__top
        self.__top = self.__top.get_next()
        self.__size -= 1
        return result.get_data()

    def push(self, value):
        """
        Purpose
                adds the given data value to the stack
        Pre-conditions:
                value: data to be added
        Post-condition:
                the value is added to the stack
        Return:
                (none)
        """
        self.__top = Node(value, self.__top)
        self.__size += 1


    def peek(self):
        """
        Purpose
                returns the value from the front of stack
                without removing it
        Post-condition:
                None
        Return:
                the value at the front of the stack
        """
        assert not self.is_empty(), 'peeked an empty stack'
        return self.__top.get_data()

    def to_string(self):
        """
        Purpose:
                Create a string representation of the Stack.  E.g.,
                [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
                where 1 is the top of the stack and 3 is the end of the stack
        Post_conditions:
                None
        Return: A string representation of the stack.
        """
        # special case: empty stack
        if self.is_empty():
            result = 'EMPTY'
        else:
            # walk along the chain
            walker = self.__top

            value = walker.get_data()
            result = '[ ' + str(value) + ' |'

            while walker.get_next() is not None:
                walker = walker.get_next()

                value = walker.get_data()
                result += ' *-]-->[ ' + str(value) + ' |'

            # at the end of the stack, use '/'
            result += ' / ]'

        return result
