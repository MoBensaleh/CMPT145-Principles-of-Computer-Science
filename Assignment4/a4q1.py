# CMPT 145 Assignment 4 Question 1
# Mohamed Bensaleh
# Mob127
# 11254030

import TStack as Stack

def main():
    '''
    Purpose: Displays lines from file in reversed order as well as the characters for each word
    Pre-conditions: none
    Post-conditions: none
    :return: none
    '''
    f =open("months.txt","r")
    Mainstack=Stack.create()
    for line in f.readlines():
        line=line.strip()#To remove extra spaces to it
        l=[]
        for word in line.split(" "):
            substack=Stack.create()
            for char in word:
                Stack.push(substack,char)
            #To get reversed word pop all chars
            reversedWord=""
            for i in range(Stack.size(substack)):
                reversedWord+=Stack.pop(substack)
            l.append(reversedWord)
        lineWithReversedWords=" ".join(l)
        Stack.push(Mainstack,lineWithReversedWords)
    #printing on console/Terminal
    for i in range(Stack.size(Mainstack)):
        print(Stack.pop(Mainstack))


if __name__ == '__main__':
    main()


