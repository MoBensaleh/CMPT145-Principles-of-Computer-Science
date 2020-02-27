# Mohamed Bensaleh
# CMPT 145 assignment 8
# Mob127
# 11254030


def path_to(tnode,value):
    '''
    Purpose:
        Determines if a given value appears in the tree and returns a tuple with a list of the
        data values that appear in the path.
    Pre-Conditions:
        :param tnode: A tree node
        :param value: given value
    Post-Conditions: none
    :return: a tuple with a true/false and the list of the data values from the path if it is true.
    '''
    #None then return false
    if(tnode==None):
        return (False,None)
    #if value is matching then add that value to the list and return (true,alist)
    if tnode.value == value:
        return (True,[value])
    k=path_to(tnode.left,value)
    if(k[0]==True):
        alist=k[1]
        alist.append(tnode.value)
        return (True,alist)
    k=path_to(tnode.right,value)
        #if true then add node value and return
    if(k[0]==True):
        alist=k[1]
        alist.append(tnode.value)
        return (True,alist)
        #None of the both left & right subtrees contains value so return false
    return (False,None)



def find_path(tnode,val1,val2):
    '''
    Purpose:
        Determines the path between any the node containing val1 and the node containing val2
    Pre-Conditions:
        :param tnode: A tree node
        :param val1: first given value
        :param val2: second given value
    Post-conditions: none
    :return: returns the path between any the node containing val1 and the node containing val2
    '''
    #find path to val1
    path1=path_to(tnode,val1)
    #if false then val1 is not in the binary tree, so return None
    if(path1[0]==False):
        return None
    #find path to val2
    path2=path_to(tnode,val2)
    #if false return None
    if(path2[0]==False):
        return None
    alist1,alist2=path1[1],path2[1]
#traverse from the backwards as the rightmost element is the root and
#run the loop until the nodes are not equal
    i,j=len(alist1)-1,len(alist2)-1
    while(i>-1 and j>-1):
        if(alist1[i]!=alist2[j]):
            break
    i-=1
    j-=1
#Since the common node should print only once so we add that value in l1
    l1=alist1[:i+2]
    l2=alist2[:j+1]
    return l1+l2[::-1]

