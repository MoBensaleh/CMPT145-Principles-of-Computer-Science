import treenode as tn

def build_lecture_example():
    """returns the example found in the lecture slides"""
    atree = tn.create(2)
    a = tn.create(7)
    b = tn.create(5)
    tn.set_left(atree, a)
    tn.set_right(atree, b)
    c = tn.create(11)
    d = tn.create(6)
    tn.set_left(a, c)
    tn.set_right(a, d)
    return atree


def build_turtle():
    atree = tn.create('t', tn.create('u', tn.create('t'), tn.create('r')), tn.create('e', tn.create('l'), None))
    return atree

# a larger more e-xtree-me tree
def build_xtree_me():
    """builds a slightly larger, more or less undistinguished tree"""
    xtree = tn.create(5,
                  tn.create(1,None,
                            tn.create(4,
                                      tn.create(3,tn.create(2,None,None),None),
                                      None)),
                  tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                              tn.create(1,tn.create(3,None,None),tn.create(3,None,None))))
    return xtree


# a tree with some meaning
def build_expr_tree():
    """builds a particular tree that reflects an arithmetic expression"""
    expr_tree = tn.create('*',
                      tn.create('+',
                                tn.create('+',
                                          tn.create(2.0, None, None),
                                          tn.create(3.0, None, None)),
                                tn.create(3.0, None, None)),
                      tn.create('+',
                                tn.create(4.0, None, None),
                                tn.create('/',
                                          tn.create(2.0, None, None),
                                          tn.create('+',
                                                    tn.create(89.0, None, None),
                                                    tn.create(3.0, None, None)))))
    return expr_tree

def treeify(alist):
    """
    Create a tree using the given list.
       The first node in the tree is the data value of the root.
       The first half of the remaining nodes form the left subtree.
       The second half of the remaining nodes form the right subtree.
       If the list has an even length, the left subtree will be slightly bigger then the right

    :param alist: a Python list
    :return: a primitive tree structure (tnode)
    """

    if alist == []:
        return None
    elif len(alist) == 1:
        return tn.create(alist[0])
    else:
        mid = 1 + len(alist)//2
        return tn.create(alist[0], treeify(alist[1:mid]), treeify(alist[mid:]))


def build_complete(height, d=0):
    """
    Create a complete binary tree of the given height.
    The data value for the root of the tree is d
    :param height: a non-negative integer
    :param d: an integer, used as the value for the root of the tree
    :return: a complete primitive binary tree whose root has data value d
    """
    if height == 0:
        return None
    else:
        return tn.create(d,build_complete(height-1,2*d+1), build_complete(height-1,2*d+2))


def build_fibtree(n):
    """
    Build a tree whose structure represents the Fibonacci numbers.
    The root of the tree has data value Fib(n).

    :param n: a non-negative integer
    :return: a primitive binary tree whose structure reflects the calculation of fib(n)
    """
    if n <= 1:
        return tn.create(n)
    else:
        ltree = build_fibtree(n-1)
        rtree = build_fibtree(n-2)
        return tn.create(tn.get_data(ltree)+tn.get_data(rtree), ltree, rtree)

