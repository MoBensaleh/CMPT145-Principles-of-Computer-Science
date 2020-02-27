# Mohamed Bensaleh
# CMPT 145
# Mob127
# 11254030


def create():
    """
        Purpose:
                Create a Statistics record.
        Pre-conditions:
                (none)
        Post-conditions:
                a new record is allocated
        Return:
                A reference to a Statistics record.
        """
    b = {}
    b['count'] = 0  # how many data values have been seen
    b['avg'] = 0  # the running average so far
    b['max'] = None # the running max value so far
    b['min'] = None # the running min value so far
    return b


def add(stat, value):
    """
        Purpose:
                Use the given value in the calculation of statistics.
        Pre-Conditions:
                stat: a Statistics record
                value: the value to be added
        Post-Conditions:
                none
        Return:
                none
        """
    stat['count'] += 1
    k = stat['count']  # convenience
    diff = value - stat['avg']  # convenience
    stat['avg'] += diff / k
    if stat['max']:
        stat['max'] = max(stat['max'], value)
    else:
        stat['max'] = value
    if stat['min']:
        stat['min'] = min(stat['min'], value)
    else:
        stat['min'] = value


def mean(stat):
    """
        Purpose:
                Return the mean of all the values seen so far.
        Pre-conditions:
                stat: the Statistics record
        Post-conditions:
                (none)
        Return:
                The mean of the data seen so far.
                Note: if no data has been seen, 0 is returned.
                This is clearly false.
        """
    return stat['avg']


def count(stat):
    """
        Purpose:
                Return the number of values recorded till now
        Pre-conditions:
                stat: the Statistics record
        Post-conditions:
                (none)
        Return:
                count of values recorded till now
                Note: if no data has been seen, 0 is returned.
        """
    return stat['count']


def maximum(stat):
    """
        Purpose:
                Return the maximum values recorded until now
        Pre-conditions:
                stat: the Statistics record
        Post-conditions:
                (none)
        Return:
                maximum value from stat that has been seen until now
                Note: if no data has been seen, None is returned.
        """
    return stat['max']


def minimum(stat):
    """
        Purpose:
                Return the minimum values recorded until now
        Pre-conditions:
                stat: the Statistics record
        Post-conditions:
                (none)
        Return:
                minimum value from stat has been seen until now
                Note: if no data has been seen, None is returned.
        """
    return stat['min']

