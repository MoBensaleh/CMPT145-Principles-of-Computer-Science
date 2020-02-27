# CMPT 145.201901 Assignment 4 Question 5
# Test script for FCQueue implementation

import FCQueue as Queue

###################### UNIT TESTING ############################
################################################################
######################## Testing create() ######################
capacity = 5
queue = Queue.create(capacity)

####################### test case
# check that it's empty
result = len(queue['storage'])
expected = 0
reason = 'create(): length of new queue should be 0'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# check that the capacity is stored correctly
result = queue['capacity']
expected = capacity
reason = 'create(): capacity of new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

########################################################################
######################## Testing is_empty() ######################
# example showing use of create()
capacity = 5
queue = Queue.create(capacity)

####################### test case
# check that it's empty
result = Queue.is_empty(queue)
expected = True
reason = 'is_empty(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

#######################
# example without use of create()
# testing the implementation, we can exploit our knowledge of the record
capacity = 5
queue = {'storage' : [], 'capacity' : capacity}

####################### test case
# check that it's empty
result = Queue.is_empty(queue)
expected = True
reason = 'is_empty(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


#######################
# a non-empty queue, constructed by hand
capacity = 5
queue = {'storage' : [1,2], 'capacity' : capacity}

####################### test case
# check that it's empty
result = Queue.is_empty(queue)
expected = False
reason = 'is_empty(): non-empty queue with 2 values'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

########################################################################
######################## Testing size() ######################
# example showing use of create()
capacity = 5
queue = Queue.create(capacity)

####################### test case
# check that it's empty
result = Queue.size(queue)
expected = 0
reason = 'size(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

#######################
# example without use of create()
# testing the implementation, we can exploit our knowledge of the record
capacity = 5
queue = {'storage' : [], 'capacity' : capacity}

####################### test case
# check that it's empty
result = Queue.size(queue)
expected = 0
reason = 'size(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


#######################
# a non-empty queue, constructed by hand
capacity = 5
queue = {'storage' : ['a', 'zzz', 'frotz'], 'capacity' : capacity}

####################### test case
# check size
result = Queue.size(queue)
expected = 3
reason = 'size(): non-empty queue size 3'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


########################################################################
######################## Testing peek() ######################
# a non-empty queue, constructed by hand
capacity = 5
queue = {'storage' : ['a', 'zzz', 'frotz'], 'capacity' : capacity}

####################### test case
# check the first thing
result = Queue.peek(queue)
expected = 'a'
reason = 'peek(): multiple values'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# a non-empty queue, constructed by hand
capacity = 5
queue = {'storage' : [42], 'capacity' : capacity}

# check the first thing
result = Queue.peek(queue)
expected = 42
reason = 'peek(): single value'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


########################################################################
######################## Testing dequeue() ######################
# a non-empty queue, constructed by hand
capacity = 5
queue = {'storage' : ['a', 'zzz', 'frotz'], 'capacity' : capacity}

####################### test case
# grab the first thing
result = Queue.dequeue(queue)
expected = 'a'
reason = 'dequeue(): multiple values'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

# a non-empty queue, constructed by hand
capacity = 5
queue = {'storage' : [42], 'capacity' : capacity}

####################### test case
# grab the first thing
result = Queue.dequeue(queue)
expected = 42
reason = 'dequeue(): single value'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


########################################################################
######################## Testing enqueue() ######################
# example showing use of create()
capacity = 5
queue = Queue.create(capacity)

#######################
# add to empty queue
Queue.enqueue(queue, 123)

####################### test case
# no return value so we look at the record
result = queue['storage'][-1]
expected = 123
reason = 'enqueue(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


# a non-empty queue, constructed by hand
capacity = 5
queue = {'storage' : ['a', 'zzz', 'frotz'], 'capacity' : capacity}

####################### test case
# add to queue
Queue.enqueue(queue, 'xyzzy')

# no return value so we look at the record
result = queue['storage'][-1]
expected = 'xyzzy'
reason = 'enqueue(): non-empty queue, below capacity'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

# a non-empty queue, constructed by hand
capacity = 3
queue = {'storage' : ['a', 'zzz', 'frotz'], 'capacity' : capacity}

####################### test case
# add to queue
Queue.enqueue(queue, 'xyzzy')

# no return value so we look at the record
result = queue['storage'][-1]
expected = 'frotz'
reason = 'enqueue(): non-empty queue, at capacity'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)




###################### INTEGRATION TESTING ############################
################################################################
capacity = 5
queue = Queue.create(capacity)

####################### test case
# check that it's empty
result = Queue.is_empty(queue)
expected = True
reason = 'create(), is_empty(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# check that it's empty
result = Queue.size(queue)
expected = 0
reason = 'create(), size(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

################################################################
capacity = 5
queue = Queue.create(capacity)

Queue.enqueue(queue,'aval')

####################### test case
# check that it's not empty
result = Queue.is_empty(queue)
expected = False
reason = 'create(), enqueue(), is_empty(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# check that it's empty
result = Queue.size(queue)
expected = 1
reason = 'create(), enqueue(), is_empty(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# check that it's empty
result = Queue.peek(queue)
expected = 'aval'
reason = 'create(), enqueue(), peek(): new queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)



################################################################
Queue.enqueue(queue,'bval')

####################### test case
# check that it's not empty
result = Queue.is_empty(queue)
expected = False
reason = 'create(), enqueue(), is_empty(): existing queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# check size
result = Queue.size(queue)
expected = 2
reason = 'create(), enqueue(), size(): existing queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# what's first
result = Queue.peek(queue)
expected = 'aval'
reason = 'create(), enqueue(), peek(): existing queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

################################################################
Queue.enqueue(queue,'ta-da!')

####################### test case
# check that it's not empty
result = Queue.is_empty(queue)
expected = False
reason = 'create(), enqueue(), is_empty(): existing queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# check size
result = Queue.size(queue)
expected = 3
reason = 'create(), enqueue(), size(): existing queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# grab first thing
result = Queue.dequeue(queue)
expected = 'aval'
reason = 'create(), enqueue(), dequeue(): existing queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# what's first?
result = Queue.peek(queue)
expected = 'bval'
reason = 'create(), enqueue(), dequeue(), peek(): existing queue'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

################################################################
capacity = 5
queue = Queue.create(capacity)
Queue.enqueue(queue, 1)
Queue.enqueue(queue, 2)
Queue.enqueue(queue, 3)
Queue.enqueue(queue, 4)
Queue.enqueue(queue, 5)
Queue.enqueue(queue, 'too many')


####################### test case
# check that it's not empty
result = Queue.is_empty(queue)
expected = False
reason = 'create(), enqueue(), is_empty(): queue at capacity'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)

####################### test case
# check size
result = Queue.size(queue)
expected = 5
reason = 'create(), enqueue(), size(): queue at capacity'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


####################### test case
# what's first
result = Queue.peek(queue)
expected = 1
reason = 'create(), enqueue(), peek(): queue at capacity'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)


####################### test case
# inspect the last element enqueued
result = queue['storage'][-1]
expected = 5
reason = 'create(), enqueue(): last element of queue at capacity'

if result != expected:
    print('Test failed: Received', result, 'Expected', expected, '--', reason)



print('Testing completed')