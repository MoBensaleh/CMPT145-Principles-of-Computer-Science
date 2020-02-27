import node as node

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain. E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain: A node-chain, possibly empty
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        return 'EMPTY'

    s = '[ ' + str(node.get_data(node_chain)) + ' | '

    if node.get_next(node_chain) == None:
        s += '/ ]'
    else:
        s += '* -]-->' + to_string(node.get_next(node_chain))
    return s


def copy_chain(node_chain):
    """
    Purpose:
        Make a new node chain with the same values as in node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
    Post-conditions:
        None
    Return:
        :return: A copy of node chain, with new nodes, but the same data.
    """
    if node_chain is None:
        return node_chain

        # create a new node corresponding to current node
    head = node.create(node.get_data(node_chain))

    # create duplicate chain for remaining nodes.
    remaining_chain = copy_chain(node.get_next(node_chain))

    # set remaining chain as next node to head node.
    node.set_next(head, remaining_chain)

    return head


def replace(node_chain, target, replacement):
    """
    Purpose:
        Replace every occurrence of data target in node_chain with data value
        The chain should change data values only!
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a data value
        :param value: a data value
    Post-conditions:
        The node-chain is changed, by replacing target with value everywhere.
    Return:
        :return: None
    """
    # check if list is not empty
    if node_chain is not None:

        # if current node's data needs to be replaced
        if node.get_data(node_chain) == target:
            node.set_data(node_chain, replacement)

        # do the replacement in remaining list
        replace(node.get_next(node_chain), target, replacement)

    # return the passed node list
    return node_chain
