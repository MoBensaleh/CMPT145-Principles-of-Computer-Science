# CMPT 145: Internal Definitions

# The function split() is useful for quick sort algorithms!

def split(alist, pivot):
    """
    Purpose:
        Split the given alist into three lists:
            greater than pivot
            equal to pivot
            less than pivot 
    Preconditions:
        alist: a list of values
        pivot: a value to compare with
    Return:
        a tuple of lists (ls, eq, gs) where 
            ls contains all the values in alist less than the pivot
            eq contains all the values in alist equal to the pivot
            gs contains all the values in alist greater than the pivot
    """
    gs = []
    es = []
    ls = []

    def place(x, pivot):
        if x == pivot:
            es.append(x)
        elif x < pivot:
            ls.append(x)
        else:
            gs.append(x)

    for x in alist:
        place(x, pivot)
    return ls, es, gs

print(split([1,2,3,4,5,6,7,8,9], 5))

