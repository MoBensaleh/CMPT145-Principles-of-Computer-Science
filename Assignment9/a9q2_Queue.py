# Mohamed Bensaleh
# CMPT 145 Assignment 9
# Mob127
# 11254030


from a9q2_Container import Container


class Queue(Container):

    def __init__(self):
        """
        Purpose
                Constructor: creates an empty queue
        Post-condition:
                queue is created with no values inside
        Return
                None
               """
        Container.__init__(self)

    def dequeue(self):
        """
        Purpose
                removes and returns a data value from the current queue
        Post-condition:
                the first value enqueued in queue is removed from the queue
        Return:
                the first value in the queue, or None
        """
        assert not Container.is_empty(self), 'dequeued an empty queue'
        return Container.removeFront(self)

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
        Container.insertRear(self, value)

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
        assert not Container.is_empty(self), 'peeked into an empty queue'
        return Container.front(self)


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
