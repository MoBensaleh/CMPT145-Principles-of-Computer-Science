# Mohamed Bensaleh
# CMPT 145 Assignment 9
# Mob127
# 11254030


from Node import Node


class Queue:
    '''
    Queue class represent a First In First Out structure.
    This has common methods such as to enqueue the data,
    dequeue the values, find size and check if queue is empty.
    '''

    def __init__(self):
        """
        Purpose
                Constructor: creates an empty queue
        Post-condition:
                queue is created with no values inside
        Return
                None
        """
        self.__front = None
        self.__back = None
        self.__size = 0

    def size(self):
        """
        Purpose
                returns the number of data values in the queue
        Post-condition:
                None
        Return:
                The number of data values in the queue
        """
        return self.__size

    def is_empty(self):
        """
        Purpose
                checks if the queue has no data in it
        Post-condition:
                None
        Return:
                True if the queue has no data, or false otherwise
        """
        return self.__size == 0

    def dequeue(self):
        """
        Purpose
                removes and returns a data value from the current queue
        Post-condition:
                the first value enqueued in queue is removed from the queue
        Return:
                the first value in the queue, or None
        """
        assert not self.is_empty(), 'dequeued an empty queue'

        result = self.__front
        self.__front = self.__front.get_next()
        self.__size -= 1
        return result.get_data()

    def enqueue(self, value):
        """
        Purpose
                adds the given data value to the back of the queue
        Pre-conditions:
                value: data to be added
        Post-condition:
                the value is added to the back of queue
        Return:
                (none)
        """
        # create a new node with value
        new_node = Node(value)

        # if queue is initially empty.
        if self.__size == 0:
            self.__front = new_node
        else:
            # set the new node as the last node
            self.__back.set_next(new_node)

        # update the last node and size of queue
        self.__back = new_node
        self.__size += 1

    def peek(self):
        """
        Purpose
                returns the value from the front of queue
                without removing it
        Post-condition:
                None
        Return:
                the value at the front of the queue
        """
        assert not self.is_empty(), 'peeked into an empty queue'
        return self.__front.get_data()

    def to_string(self):
        """
        Purpose:
                Create a string representation of the queue.  E.g.,
                [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
                where 1 is the top of the queue and 3 is the end of the queue
        Post_conditions:
                None
        Return: A string representation of the queue.
        """
        # special case: empty queue
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

            # at the end of the queue, use '/'
            result += ' / ]'

        return result