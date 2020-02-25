# CMPT 145: Internal definitions


def split(data, pivot, smaller, equal, bigger):
    for v in data:
        if v < pivot:
            smaller.append(v)
        elif v == pivot:
            equal.append(v)
        else:
            bigger.append(v)
    return smaller, equal, bigger
        

def qsort2(data):
    """
    Purpose:
        Returns a list of the data values in sorted order.
    Preconditions:
        data: a list of values comparable by <, ==
    Postconditions:
        The original data is not affected
    Return:
        A list of the same values as given, but in sorted order.
    """
    if len(data) == 0 or len(data) == 1:
        return data
    else:
        pivot = data[0]
        smaller, equal, bigger = split(data, pivot, [], [], [])
        return qsort2(smaller) + equal + qsort2(bigger)


if __name__ == '__main__':
    test_suite = [
        {'inputs': [],
         'outputs': [],
         'reason': 'empty list'},
        {'inputs': [1],
         'outputs': [1],
         'reason': 'list of one'},
        {'inputs': [1,0],
         'outputs': [0,1],
         'reason': 'list of two, out of order'},
        {'inputs': [0,1],
         'outputs': [0,1],
         'reason': 'list of two, in order'},
        {'inputs': [0,1,2],
         'outputs': [0,1,2],
         'reason': 'list of three, in order'},
        {'inputs': [2,0,1],
         'outputs': [0,1,2],
         'reason': 'list of three, out of order'},
        {'inputs':  [2,2,2,2,2,2,2],
         'outputs': [2,2,2,2,2,2,2],
         'reason': 'all the same'},
         {'inputs':  [1,2,3,4,5,6,7,8],
         'outputs': [1,2,3,4,5,6,7,8],
         'reason': 'already in order'},
         {'inputs':  [8,7,6,5,4,3,2,1],
         'outputs': [1,2,3,4,5,6,7,8],
         'reason': 'reverse order'},
         {'inputs':  [1,4,6,2,8,7,3,5],
         'outputs':  [1,2,3,4,5,6,7,8],
         'reason': 'randomish order'}
    ]
    for case in test_suite:
        case_input = case['inputs']
        case_expected = case['outputs']
        test_output = qsort2(case_input)
        if test_output != case_expected:
            print("Test fault on", case_input, "returned:", test_output, 'should have been', case_expected, 'Reason:', case['reason'])
    print('***Testing complete***')
