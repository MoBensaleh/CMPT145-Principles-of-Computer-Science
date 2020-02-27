# CMPT 145 Assignmment 4 Question 3
# Mohamed Bensaleh
# Mob127
# 11254030

import a4q2 as Stack
def Calculate():
    calculate = 'yes'
    print("Welcome to Calculator!")
    print('Do you want to perform a calculation?(yes or no)')
    calculate = str.lower(input())

    while calculate == 'yes' or calculate == 'y':
        print('Do you have a calculation?(yes or no)')
        calculate = str.lower(input())
        if calculate == 'quit' or calculate == 'no':
            print('Thanks for using Calculator!')
            exit()

        exp = input('Enter an expression:', )
        print (Stack.evaluate(exp))

    if calculate == 'quit' or calculate == 'no':
        print('Thanks for using Calculator!')


Calculate()
