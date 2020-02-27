# Mohamed Bensaleh
# CMPT 145 Assignment 9
# Mob127
# 11254030


from a9q2_Container import Container


class Stack(Container):

    def __init__(self):
        """
        Purpose
                Constructor: creates an empty stack
        Post-condition:
                Stack is created with no values inside
        Return
                None
        """
        Container.__init__(self)

    def pop(self):
        """
        Purpose
                removes and returns a data value from the current stack
        Post-condition:
                the first value is removed from the stack
        Return:
                the first value in the stack, or None
        """
        assert not Container.is_empty(self), 'popped an empty stack'
        return Container.removeFront(self)

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
        Container.insertFront(self, value)

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
        assert not Container.is_empty(self), 'peeked into an empty stack'
        return Container.front(self)

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




