# CMPT 145: Laboratory Material: Memoization

import treenode as tn

def fib(n):
    """
    Purpose:
        Calculate the nth Fibonacci number
        The Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, ...
    Preconditions:
        :param n: a non-negative integer
    Return:
        :return: the nth Fibonacci number, starting with fib(0) = 0
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        f1 = fib(n-1)
        f2 = fib(n-2)
        return f1+f2

def fibtree(n):
    """
    Purpose:
        Create a Fibonacci tree for n
    Preconditions:
        :param n: a non-negative integer
    Return:
        :return: the nth Fibonacci number, starting with fib(0) = 0
    """
    if n == 0 or n == 1:
        # put brackets around the leaf nodes so they stand out
        return tn.create('('+str(n)+')')
    else:
        tl = fibtree(n-1)
        tr = fibtree(n-2)
        return tn.create(str(n), tl, tr)

def fibm(n):
    """
    Purpose:
        Calculate the nth Fibonacci number.
        The Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, ...
    Preconditions:
        :param n: a non-negative integer
    Return:
        :return: the nth Fibonacci number, starting with fib(0) = 0
    """
    # the memo will make the calculation faster
    memo = {}
    def memoized(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n in memo:
            return memo[n]
        else:
            f1 = memoized(n-1)
            f2 = memoized(n-2)
            memo[n] = f1+f2
            return f1+f2
    return memoized(n)


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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return moosonacci(n-1) + moosonacci(n-2) + moosonacci(n-3)

 
def fibmtree(n):
    """
    Purpose:
        Create a Fibonacci tree for n showing memoization.
    Preconditions:
        :param n: a non-negative integer
    Return:
        :return: the nth Fibonacci number, starting with fib(0) = 0
    """
    memo = {}
    def memoized(n):
        if n == 0 or n == 1:
            # put brackets around the leaf nodes so they stand out
            return tn.create('('+str(n)+')')
        elif n in memo:
            # put brackets around memo lookups so they stand out
            return tn.create('['+str(n)+']')
        else:
            tl = memoized(n-1)
            tr = memoized(n-2)
            memo[n] = True
            return tn.create(n, tl, tr)
    return memoized(n)


def display_tree(atnode):
    """
    Purpose:
        Display a tree.  
    Preconditions:
        :param atnode: A treenode
    Postconditions:
        The tree is displayed on the output.  
        Root on the left.
        Right subtree is above the root
        Left subtree is below the root
        Subtrees are indented
        No branches drawn.
    Return:
        :return: None
    """
    def disp(tnode, indent):
        if tnode is not None:
            disp(tn.get_right(tnode), indent+2)
            print(' '*(indent-1), tn.get_data(tnode))
            disp(tn.get_left(tnode), indent+2)
    disp(atnode, 0)

if __name__ == '__main__':
    n = int(input('Enter a positive integer for Fibonacci: '))
    print('fibonacci tree for n =', n)
    display_tree(fibtree(n))
    print('memoized fibonacci tree for n =', n)
    display_tree(fibmtree(n))
    


