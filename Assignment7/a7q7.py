def marioCount(rows, cols):
    if(rows == 1 or cols == 1):
        return 1

    return marioCount(rows-1, cols) + marioCount(rows, cols-1)

#  main function to be executed
print(marioCount(3, 3))
print(marioCount(4,4))
print(marioCount(10,12))


