#CMPT 145 Assignment 4 question 2 Testing
# Mohamed Bensaleh
# Mob127
# 11254030

import a4q2 as Stack
def test():
    print("--------TESTING INDIVIDUAL OPERATORS----------")
    print('"( 3 + 6 )" =', Stack.evaluate("( 3 + 6 )"))
    print('"( 3 - 5 )" =', Stack.evaluate("( 3 - 5 )"))
    print('"( 3 * 6 )" =', Stack.evaluate("( 3 * 6 )"))
    print('"( 3 / 5 )" =', Stack.evaluate("( 3 / 5 )"))
    assert Stack.evaluate("( 3 + 6 )") == 9
    assert Stack.evaluate("( 3 - 5 )") == -2
    assert Stack.evaluate("( 3 * 6 )") == 18
    assert Stack.evaluate("( 3 / 5 )") == 0.6
    print("--------OPERATORS WORK CORRECTLY----------")
    print()
    print("--------TESTING EXPRESSIONS------------")
    print('"( ( 11 / 12 ) * 13 ) " = ', Stack.evaluate("( ( 11 / 12 ) * 13 ) "))
    print('"( ( 11 + 12 ) - 13 ) " = ', Stack.evaluate("( ( 11 + 12 ) - 13 ) "))
    print('"( ( 11 + 12 ) * 13 ) " = ', Stack.evaluate("( ( 11 + 12 ) * 13 ) "))

    assert Stack.evaluate("( ( 11 / 12 ) * 13 ) ") == 11.916666666666666
    assert Stack.evaluate("( ( 11 + 12 ) - 13 ) ") == 10.0
    assert Stack.evaluate("( ( 11 + 12 ) * 13 ) ") == 299.0
    print("--------EXPRESSIONS WORK CORRECTLY---------")


test()
