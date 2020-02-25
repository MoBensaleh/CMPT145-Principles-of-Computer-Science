
def moosonacci(n):
    """
    Purpose:
        Calculate the nth Moosonacci number
        The Moosonacci numbers are: 0, 1, 2, 3, 6, 11, 20, 37, ...
    Preconditions:
        :param n: a non-negative integer
    Return:
        :return: the nth Moosonacci number, starting with moos(0) = 0
    """
    memo = {}
    def memoized(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n in memo:
            return memo[n]
        else:
            f1 = memoized(n - 1)
            f2 = memoized(n - 2)
            f3 = memoized(n - 3)
            memo[n] = f1+f2+f3
            return f1+f2+f3
    return memoized(n)

print(moosonacci(38))