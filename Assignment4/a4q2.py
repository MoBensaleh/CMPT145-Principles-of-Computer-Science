# CMPT 145 Assignment 4 Question 2
# Mohamed Bensaleh
# Mob127
# 11254030

def isfloat(str_val):
    """
    Purpose:
        Check whether a string represents a floating point str_val
    Preconditions:
        str_val: a string
    Post-conditions:
        None
    Return:
        True if str_val can be converted to a floating point number
    """
    try:
        float(str_val)
        return True
    except:
        return False

import TStack as Stack
def evaluate(exp):
    '''
    Purpose:  Evaluates numerical expressions
    Pre-conditions:
        :param exp: Numerical expression to evaluate
    Post-conditions: none
    :return: Result from computation is pushed back on the numeric value stack
    '''
    # Create empty stacks
    value_stack = Stack.create()
    operator_stack = Stack.create()

    lst = exp.split()  # Making list of characters in the expression

    for char in lst:

        if Stack.isfloat(char):
            val = float(char)
            Stack.push(value_stack, val)

        elif char == '+' or char == '-' or char == '*' or char == '/':
            Stack.push(operator_stack, char)

        elif char == ')':
            val1 = Stack.pop(value_stack)
            val2 = Stack.pop(value_stack)
            operator = Stack.pop(operator_stack)

            if operator == '+':
                result = val1 + val2
            elif operator == '-':
                val1, val2 = val2, val1
                result = val1 - val2
            elif operator == '*':
                result = val1 * val2
            elif operator == '/':
                val1, val2 = val2, val1
                result = val1 / val2
            else:
                print("Unknown operator")
                break

            Stack.push(value_stack, result)

        else:
            pass

    return (Stack.pop(value_stack))
