# CMPT 145 A4Q1 integration testing


import TStack as Stack

# CODE for integration Testing
def main():
    # Test 1 positive integers
    print("For Integration Testing:")
    print("is_empty:",Stack.is_empty(Stack.create()))
    print("size:",Stack.size(Stack.create()))
    Stack.push(Stack.create(),5)
    stack=Stack.create()
    Stack.push(stack,5)
    Stack.push(stack,6)
    print("Pop:",Stack.pop(stack))
    print("Peek:",Stack.peek(stack))


    # Test 2 negative integers
    print("For Integration Testing:")
    print("is_empty:", Stack.is_empty(Stack.create()))
    print("size:", Stack.size(Stack.create()))
    Stack.push(Stack.create(), -7)
    stack = Stack.create()
    Stack.push(stack, -7)
    Stack.push(stack, -10)
    print("Pop:", Stack.pop(stack))
    print("Peek:", Stack.peek(stack))

    # Test 3 Decimal numbers
    print("For Integration Testing:")
    print("is_empty:", Stack.is_empty(Stack.create()))
    print("size:", Stack.size(Stack.create()))
    Stack.push(Stack.create(), 0.38)
    stack = Stack.create()
    Stack.push(stack, 0.38)
    Stack.push(stack, 6.4)
    print("Pop:", Stack.pop(stack))
    print("Peek:", Stack.peek(stack))

    # Test 4 negative decimal numbers
    print("For Integration Testing:")
    print("is_empty:", Stack.is_empty(Stack.create()))
    print("size:", Stack.size(Stack.create()))
    Stack.push(Stack.create(), -5.7)
    stack = Stack.create()
    Stack.push(stack, -5.7)
    Stack.push(stack, -0.5)
    print("Pop:", Stack.pop(stack))
    print("Peek:", Stack.peek(stack))

    # Test 5 strings
    print("For Integration Testing:")
    print("is_empty:", Stack.is_empty(Stack.create()))
    print("size:", Stack.size(Stack.create()))
    Stack.push(Stack.create(), 'Apple')
    stack = Stack.create()
    Stack.push(stack, 'Apple')
    Stack.push(stack, 'Saturday')
    print("Pop:", Stack.pop(stack))
    print("Peek:", Stack.peek(stack))


if __name__ == '__main__':
    main()