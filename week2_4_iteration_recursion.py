# power
# Iteration
# Write an iterative function iterPower(base, exp) 
# that calculates the exponential base^exp 
# by simply using successive multiplication.
# For example, iterPower(base, exp) should compute base^exp
#  by multiplying base times itself exp times. 
# Write such a function below.

# This function should take in two values 
# - base can be a float or an integer; exp will be an integer >= 0. 
# It should return one numerical value. 
# Your code must be iterative - use of the ** operator is not allowed.

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    if base == 1 or exp == 0:
        return result
    else:
        for i in range(exp):
            result *= base
    return result

# recursion

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if base == 0:
        return 0
    if base == 1 or exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)


# The greatest common divisor of two positive integers is the largest integer 
# that divides each of them without remainder. 
# For example,
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
# Write an iterative function, gcdIter(a, b), 
# that implements this idea. One easy way to do this is to begin with a test value
#  equal to the smaller of the two input arguments, 
# and iteratively reduce this test value by 1 until you either reach a case 
# where the test divides both a and b without remainder, or you reach 1.

# iteration
def gcdIter(a, b):
    global gNum
    global lNum
    
    if a > b:
        gNum = a
        lNum = b
    else:
        gNum = b
        lNum = a

    while lNum > 1:
        #print('start', gNum, lNum)
        if gNum%lNum == 0:
            #print('0', gNum, lNum)
            return lNum
        elif gNum%lNum == 1:
            #print('1', gNum, lNum)
            return 1
        else:
            #print('else', gNum, lNum)
            temp = gNum
            gNum = lNum
            lNum = temp%lNum
            #print('else2', gNum, lNum)

#recursion

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a <= b:
        if b%a == 0:
            return a
        elif b%a == 1:
            return 1
        else:
            return gcdRecur(a, b%a)
    else:
        return gcdRecur(b, a)

# bisection search algorithm

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    
    mid = int(len(aStr)/2)
    # print(mid, int(len(aStr)/2), aStr[mid])
    
    if char == aStr[mid]:
        # print('equal', char, aStr[mid])
        return True
    elif char < aStr[mid]:
        # print('smaller',char, mid, aStr[:mid])
        return isIn(char, aStr[:mid])
    else:
        # print('bigger',char, mid+1, aStr[mid+1:])
        return isIn(char, aStr[mid+1:])
        
print(isIn('i', 'abdefghij'))