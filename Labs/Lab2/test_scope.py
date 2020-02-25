# CMPT 145: Scope Laboratory
# run the test below.  Add more tests.

import scope as scope

# test case 
inputs  = []
expected = []
reason = 'Empty list'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)


# test case 
inputs  = [1]
expected = []
reason = 'Singleton list'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)


# test case 
inputs  = [1, 1]
expected = [1]
reason = 'Simplest list with a duplicate'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)


# test case 
inputs  = [1, 2, 3]
expected = []
reason = 'Longer list with no duplicates'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)
          

print('*** Test script finished ***')
