# Mohamed Bensaleh
# CMPT 145
# Mob127
# 11254030

# Assignment 3: ADTs and Testing

# This script is a starter file for testing the Statistics ADT

import Statistics as Stat

#####################################################################
# test Statistics.create()
# create() has no parameters, so we only need one test case
# but we can test several things about the statistics data structure

test_create = [
    {'inputs' : [],
     'outputs':[0, 0],
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # we'll open the data structure in these tests
    # check the initial count
    if thing['count'] != expected[0]:
        print('Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the initial ave
    if thing['avg'] != expected[1]:
        print('Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.add()
# these are integration tests

test_add = [
    {'inputs' : [0],    # single value to be added
     'outputs':[1, 0], # [count, avg]
     'reason' : 'No change to avg'},
    # TODO Add more test cases
    {'inputs' : [5],
     'outputs': [1, 5],
     'reason' : "one positive integer"},
    {'inputs' : [-3],
     'outputs': [1, -3],
     'reason' : "one negative integer"},
    {'inputs' : [0.3],
     'outputs': [1, 0.3],
     'reason' : 'floating point value'},
    {'inputs' : [-0.4],
     'outputs': [1, -0.4],
     'reason' : 'negative floating point value'}
]

for t in test_add:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # now call add()
    Stat.add(thing, args_in[0])

    # we'll open the data structure in these tests
    # check the count
    if abs(thing['count'] - expected[0]) > 0.000001: # absolute difference over exact equality
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if abs(thing['avg'] - expected[1]) > 0.000001: #absolute difference
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.mean()

test_mean = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[5, 0],          #[count, avg]
     'reason' : 'All zeroes'},
    # TODO Add more test cases
    {'inputs' : [1,2,3],
     'outputs': [3, 2],
     'reason' : "positive integer values"},
    {'inputs' : [-4, -3, -2],
     'outputs': [3, -3],
     'reason' : 'negative integer values'},
    {'inputs' : [0.3, 0.2, 0.5],
     'outputs': [3, 0.333333],
     'reason' : 'floating point values'},
    {'inputs' : [-2.4, -0.7, -0.1, -0.4],
     'outputs': [4, -0.9],
     'reason' : 'negative floating point values'},
    {'inputs' : [0.4, 2.6, 9.2],
     'outputs': [3, 4.066666],
     'reason' : 'positive floating point values'},
    {'inputs' : [],
     'outputs': [0, 0],
     'reason' : 'Empty list'},
    {'inputs' : [-0.83],
     'outputs': [1, -0.83],
     'reason' : 'one floating point value'}
]

for t in test_mean:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call mean()
    result = Stat.mean(thing)

    # we'll open the data structure in these tests
    # check the count
    if abs(thing['count'] - expected[0]) > 0.000001:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if abs(thing['avg'] - expected[1]) > 0.000001:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

    # check the result of mean()
    if abs(result - expected[1]) > 0.000001:
        print('Error in mean(): expected avg', expected[1],
              ' but found ', result, '--', t['reason'])

print('*** Test script completed ***')