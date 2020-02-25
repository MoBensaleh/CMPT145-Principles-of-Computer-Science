# CMPT 145: Internal Definitions



# The Collatz Sequence 
# The collatz sequence is is defined by a simple conditional
#   Suppose N is a positive integer in the sequence
#    if N is even, the next number in the sequence is N//2
#    if N is odd, the next number in the sequence is 3*N+1
# By definition, the Collatz sequence ends when N=1.  

# For example, the Collatz sequnce starting at 5:
#   5, 16, 8, 4, 2, 1
# Depending on where the sequence starts, the numbers in the sequence
# can be quite large, and keep jumping higher and higher using the
# rule for odd numbers.  But eventually, no matter which number we try, 
# it comes back down, using the rule for even numbers.

# This is an interesting sequence because it defies our 
# current mathematics.  In practice, we can start a sequence
# at any positive integer, and eventually we get to 1.  
# However, there is currently no mathematical way to prove
# that this is true for all integers.  There may be some number
# we haven't tried yet that starts a sequence that never terminates.
# Or it may be true that there is no such number at all.  We just 
# don't know how to prove it one way or the other.  Obviously,
# we cannot simply try them all.

def collatz(a):
    """
    Purpose:
        Return the largest value in the Collatz Sequence 
        starting at a.
    Preconditions:
        a: a positive integer
    Return:
        The largest value in the Collatz sequnce starting at a
    """
    def coll_step(b):
        if b % 2 == 0:
            return b // 2
        else:
            return 3 * b + 1

    biggest = a
    while a > 1:
        a = coll_step(a)
        if a > biggest:
            biggest = a
    return biggest


if __name__ == '__main__':
    import sys as sys
    cstart = None
    if len(sys.argv) != 2:
        cstart = int(input('Where would you like to start the sequence? '))
    else:
        cstart = int(sys.argv[1])

    print('Starting at', cstart, 
          'the largest number in Collatz sequence is', collatz(cstart))
