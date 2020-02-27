# CMPT 145 Assignment 4 question 1 Testing
# Mohamed Bensaleh
# Mob127
# 11254030

#CODE For UNIT TESTING

import TStack as Stack
def main():
    # Test number 1 (positive integer)
    print("For Unit Testing:")
    stack=Stack.create()
    print("is_empty:",Stack.is_empty(stack))
    Stack.push(stack,5)
    print("size:",Stack.size(stack))
    print("is_empty:",Stack.is_empty(stack))
    print("Peek:",Stack.peek(stack))
    print("pop:",Stack.pop(stack))

    # Test Number 2 (decimal)
    print("For Unit Testing:")
    stack = Stack.create()
    print("is_empty:", Stack.is_empty(stack))
    Stack.push(stack, 0.3)
    print("size:", Stack.size(stack))
    print("is_empty:", Stack.is_empty(stack))
    print("Peek:", Stack.peek(stack))
    print("pop:", Stack.pop(stack))

    # Test Number 3 (negative integer)
    print("For Unit Testing:")
    stack = Stack.create()
    print("is_empty:", Stack.is_empty(stack))
    Stack.push(stack, -5)
    print("size:", Stack.size(stack))
    print("is_empty:", Stack.is_empty(stack))
    print("Peek:", Stack.peek(stack))
    print("pop:", Stack.pop(stack))

    # Test Number 4 (negative decimal)
    print("For Unit Testing:")
    stack = Stack.create()
    print("is_empty:", Stack.is_empty(stack))
    Stack.push(stack, -42.4)
    print("size:", Stack.size(stack))
    print("is_empty:", Stack.is_empty(stack))
    print("Peek:", Stack.peek(stack))
    print("pop:", Stack.pop(stack))

    # Test Number 5 (Strings)
    print("For Unit Testing:")
    stack = Stack.create()
    print("is_empty:", Stack.is_empty(stack))
    Stack.push(stack, 'Friday')
    print("size:", Stack.size(stack))
    print("is_empty:", Stack.is_empty(stack))
    print("Peek:", Stack.peek(stack))
    print("pop:", Stack.pop(stack))


if __name__ == '__main__':
    main()
