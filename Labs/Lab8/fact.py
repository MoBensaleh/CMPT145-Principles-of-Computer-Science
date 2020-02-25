# CMPT 145: Internal Definitions

def fact_helper(i, n, prod):
    """
    Purpose:
        Assist factorial() in the computation of n!
    Preconditions:
        i: an integer in the range 1...n
        n: the end of the range of i
        prod: the accumulated product 1 * 2 * ... * i
    Return:
        an integer, equal to n!
    """
    if i == n:
        return i*prod
    else:
        return fact_helper(i+1, n, i*prod)
 
 
def factorial(n):
    """
    Purpose:
        Calculate n!
    Preconditions:
        n: a non-negative integer
    Return:
        an integer, equal to n!
    """
    if n == 0: 
        return 1
    else:
        return fact_helper(1, n, 1)


if __name__ == '__main__':
    print("A simple demo for factorial")
    
    inputs = [0,1,2,3,4,5,6]
    expected = [1,1,2,6,24,120,720]
    for (ip,ex) in zip(inputs, expected):
        result = factorial(ip)
        if  result != ex:
            print("Error: factorial of", ip, "returned", result, "but", ex, "was expected")
        else:
            print("factorial of", ip, "returned", result)

