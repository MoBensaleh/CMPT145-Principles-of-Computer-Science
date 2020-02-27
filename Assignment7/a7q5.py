def fib(n):
    """
    Purpose: Takes non-negative integer and calculates nth fibonacci number
    Pre-conditions:
    :param n: non-negative integer
    Post-conditions: none
    :return: returns the nth fibonacci number
    """
    if n < 0:
        return 'Non negative number should be entered'
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def moos(n):
    """
    Purpose: Takes a non-negative n integer as input, and calculates the nth Moosonacci number.
    Pre-conditions:
    :param n: non-negative integer
    Post-conditions: none
    :return: returns the nth moosonacci number
    """
    if n < 0:
        return 'Non negative number should be entered'
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return moos(n-1) + moos(n-2) + moos(n-3)


def substr(c,r,s):
    """
    Purpose: takes as input a string s, a target
character c, and a replacement character r, that returns a new string with every occurrence of the
character c replaced by the character r
    Pre-conditions:
    :param c: target character
    :param r: replacement character
    :param s: string input
    Post-conditions: none
    :return: a new string with every occurrence of the character c replaced by the character r.
    """
    if s=='':
        return ''
    if s[0]==c:
        return r+substr(c,r,s[1:])
    return s[0]+substr(c,r,s[1:])


