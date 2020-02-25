# CMPT 145: ADTs
# Simple adapter for Queues

import Queue as Queue

def create():
    """
    Purpose
        creates an empty queue
    Return
        an empty queue
    """
    return Queue.create()
    
    
def add(container,value):
    """
    Purpose
        adds the given data value to the given queue
    Pre-conditions:
        container: a queue created by create()
        value: data to be added
    Post-condition:
        the value is added to the queue
    Return:
        (none)
    """
    Queue.enqueue(container,value)
    
def remove(container):
    """
    Purpose
        removes and returns a data value from the given queue
    Pre-conditions:
        container: a queue created by create()
    Post-condition:
        the first value is removed from the queue
    Return:
        the first value in the queue
    """
    return Queue.dequeue(container)
    
def is_empty(container):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        container is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    return Queue.is_empty(container)
    
def size(container):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        container: a queue created by create()
    Return:
        The number of data values in the queue
    """
    return Queue.size(container)

def peek(container):
    """
    Purpose
        Returns a refernce to the data value at the front of the queue
    Pre-conditions:
        container: a queue created by create()
    Post-condition:
        (none)
    Return:
        a reference to the first value in the queue
    """

    return container[0]
