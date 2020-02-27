# CMPT 145: Assignment 5 Question 1
# Mohamed Bensaleh
# Mob127
# 11254030

import node as node

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        value = node.get_data(walker)
        # print the data
        result = '[ ' + str(value) + ' |'
        walker = node.get_next(walker)
        while walker is not None:
            value = node.get_data(walker)
            # represent the next with an arrow-like figure
            result += ' *-]-->[ '+str(value)+' |'
            walker = node.get_next(walker)

        # at the end of the chain, use '/'
        result += ' / ]'


    return result

