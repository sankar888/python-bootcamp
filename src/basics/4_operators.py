'''
4_operators.py

This module has examples of various operators available in python

- Arithmetic Operators (+   -   *   /   //  **  %   )
- Comparision Operators (<  >   !=  <=  >=  ==)
- Bitwise operators (&  |   ~   <<  >>)
- Assignment Operators (=   +=  -=  *=  /=  //=   **=  %=   &=   <<=  >>=)
- Logical Operators (and    or  not)
- Membership Operators (in  not in)
- Identity operators (is    is not)

there is a module named operator which has functions to do basic operations. https://docs.python.org/3/library/operator.html
Also we could customize the magic functions in custom classes to use the value of custom objects with operators https://docs.python.org/3/reference/datamodel.html#object.__truediv__
'''

from utils import m_header
from utils import f_header
from decimal import Decimal

def arithmetic_operators_demo():
    '''
    Arithmentic operator are 
    +   = addition
    -   = subtraction
    *   = multiplication
    /   = division
    //  = floor division
    **  = exponential
    %   = modulo

    division will always produce a float
    All other operators
    - if there is a float in expression int is converted into float and the result will be float
    - if the result contains fraction, the result will be float
    
    modulo: The modulo operator always yields a result with the same sign as its second operand (or zero), 
    the absolute value of the result is strictly smaller than the absolute value of the second operand
    The floor division and modulo operators are connected by the following identity: x == (x//y)*y + (x%y).
    '''
    print(f'addition: 10 + 10 will result in {10 + 10}')
    print(f'addition: 0.1 + 0.2 = {0.1 + 0.2}') # to have precise computation use decimal
    print(f'addition: 10 + 10.0 will result in {10 + 10.0}') # float
    print(f'subtraction: 1 - 2.0 will result in {1 - 2.0}') # float
    print(f'multiplication: 1 * -2.0 will result in {1 * -2.0}') # float
    print(f'division: 2 / 1 will always be float {2 / 1}')
    print(f'floordivision: 3 // 2 will give the smallest integer quoficient. negative numbers will behave differently than positive numbers {3 // 2}')
    print(f'floordivision: -3 // 2 will give the smallest integer quoficient. negative numbers rounded to smallest {-3 // 2}')
    print(f'floordivision: 1 // 2 will result in {1 // 2}')
    print(f'exponential: -3 ** 2 will result in {-3 ** 2}. ** has higher precendence than -. (-3) ** 2 will result in {(-3) ** 2}')
    print(f'modulo: 1 % 2 = {1 % 2}')
    print(f'modulo: 1 % -2 = {1 % -2}')
    print(f'modulo: -4 % 3 = {(-4) % -3}') # The floor division and modulo operators are connected by the following identity: x == (x//y)*y + (x%y).

def comparision_operators_demo():
    '''
    Comparision operators are
    ==  equal to
    !=  not equal to
    <   less than
    >   greater than
    <=  less than or equal to
    >=  greater than or equal to
    '''
    # by default == checks if the value is same for basic value types like number, float string. 
    # for custom types, we could override the magic methods __eq__() and __hash__() function
    # similarly there are magic methods for all comparision operators
    print(f'equal operator: 10 == 10.0 is {10 == 10.0}')
    print(f'equal operator: 0 == -0.0 is {0 == -0.0}')
    print(f'equal operator: "a" == "a" is {"a" == "a"}')
    print(f'not equal operator: "a" != "A" is {"a" != "A"}')
    print(f'not equal operator: 1 != 1.0 is {1 != 1.0}')
    print(f'comparision operator: "a" < 10 will result in TypeError')
    print(f'comparision operator: "a" < 10 will result in TypeError')
    print(f'comparision operator: "a" < "b" is {"a" < "b"}')

    # In Python, strings are compared lexicographically, 
    # which means they are compared character by character using the Unicode (ASCII) values of each character in sequence, from left to right.
    # string comaprision is case sensitive
    print(f'comparision operator: "A" < "a" is {"A" < "a"}, "Animal" < "a" is {"Animal" < "a"}')
    print(f'string comaprision is case sensitive: "Animal" != "animal" is {"Animal" != "animal"}')

def bitwise_operators_demo():
    '''
    Bitwise operators (&  |   ~   <<  >>) in Python work at the binary level, operating on individual bits of integer values
    Bitwise operators only work with integer values
    '''
    print(f'5 (0101) & 3 (0011) = {5 & 3} (0001)') # Sets each bit to 1 if both bits are 1.
    print(f'5 (0101) | 3 (0011) = {5 | 3} (0111)') # Sets each bit to 1 if at least one of the bits is 1.
    print(f'5 (0101) ^ 3 (0011) = {5 ^ 3} (0110)') # Sets each bit to 1 if only one of the bits is 1.
    print(f'~5 (0101) = {~5} (1010)') # Inverts all the bits
    print(f'5 (0101) << 1 = {5 << 1} (1010)') # Shifts bits to the left, filling with 0s on the right
    print(f'5 (0101) >> 2 = {5 >> 1} (0010)') # Shifts bits to the right, discarding bits shifted off.

def assignment_operators_demo():
    '''
    Assignment operator assign values to a variable
    the primary assignment operator is =. it could be combined with arihtmentic and bitwise operator to create multiple assignment operator
    Assignment operators are (=   +=  -=  *=  /=  //=   **=  %=   &=   <<=  >>=)
    '''
    a = 10
    # a = a + 1
    a += 1
    print(f'assignment operator: {a}')


def logical_operators_demo():
    '''
    Logical operators: (and    or  not)
    Logical operators in Python are used to combine or modify conditions (expressions that evaluate to True or False). 
    They help in controlling the flow of a program by creating more complex conditional statements.
    '''
    print(f'logical opeator: 1 < 2 and 1 < 3 will evaluate to {1<2 and 1<3}')
    print(f'logical operator: 1 and 3 will evaluate to {1 and 3}') # 3 because and will evaluate both condition
    print(f'logical operator: 1 or 3 will evaluate to {1 or 3}') # 1 or will stop at the first non false value. All non zero values are consider thuth values in python
    print(f'logical operator: not 0 will evaluate to {not 0}') # True

def membership_operators_demo():
    '''
    membership operators: (in  not in) evaluate if a value is present in collections (list, set, tuple, dict, str)
    You can also implement membership testing in custom classes by defining the __contains__ method
    '''
    print(f'abc in abcd = {"abc" in "abcd"}') # True
    print(f'A in abcd = {"A" in "abcd"}') # False
    print(f'1 in [1,2,3,4] = {1 in [1,2,3,4]}') # True
    print(f'[1,2] in [1,2,3,4] = {[1,2] in [1,2,3,4]}') # False, because in checks for individual elements
    print(f'(1,2) in [1, (1,2), 3, 4] = {(1,2) in [1, (1,2), 3, 4]}') # True
    print(f'1 in dict(1: "one", 2: "two", 3: "three") = { 1 in {1: "one", 2: "two", 3: "three"}}')

def identity_operators_demo():
    '''
    identity operators (is    is not)
    is      - Returns True if both variables point to the same object (i.e., have the same memory address).
    is not  - Returns True if both variables reference different objects. Useful when you want to confirm that two variables do not reference the same object.
    '''
    a, b = 10, 10.0
    print(f'a is b = {a is b}')
    a, b = 10, 12-2
    print(f'a is b = { a is b}') # True, as numbers are immutable and only created if needed, id(a) == id(b)
    print(f'[1,2,3] is [1,2,3] = {[1,2,3] is [1,2,3]}') # False as list in mutable
    print(f'(1,2,3) is (1,2,3) = {(1,2,3) is (1,2,3)}') # tuples are immutable, there is no need to create anoher if one already exists in current scope
    print(f'tuple(range(1,3)) is tuple(range(1,3)) = {tuple(range(1,3)) is tuple(range(1,3))}') # False, tuple function might have created new objects

def operators_precedence_demo():
    '''
    Precedence Level	Operators	Description
    1	                ()	                                            Parentheses (grouping)
    2	                **	                                            Exponentiation
    3	                +x, -x, ~x	                                    Unary plus, minus, bitwise NOT
    4	                *, /, //, %	                                    Multiplication, division, floor division, modulus
    5	                +, -	                                        Addition and subtraction
    6	                <<, >>	                                        Bitwise shifts (left, right)
    7	                & | ^	                                        Bitwise AND OR XOR
    8	                ==, !=, >, <, >=, <=, is, is not, in, not in	Comparisons and identity/membership
    9	                not	                                            Logical NOT
    10	                and	                                            Logical AND
    11	                or	                                            Logical OR
    12	                =, +=, -=, *=, /=, etc.	                        Assignment operators
    13	                ,	                                            Expression separators
    when all operators have same presedence the expression is evaluated fromleft to right
    '''
    print(f'-3 * 4          = {-3 * 4}') # -12
    print(f'1 + -3 * 4      = {1 + -3 * 4}') # -11
    print(f'(-1 + 3) * 4    = {(-1 + 3) * 4}') # 8
    print(f'-1 + 3 * 4 / 2  = {(-1 + 3) * 4 / 2}') # 4.0

if __name__ == '__main__':
    m_header('Python Operators')
    f_header('arithmentic operators', arithmetic_operators_demo)
    arithmetic_operators_demo()

    f_header('comparision operators', comparision_operators_demo)
    comparision_operators_demo()

    f_header('bitwise operators', bitwise_operators_demo)
    bitwise_operators_demo()

    f_header('logical operators', logical_operators_demo)
    logical_operators_demo()

    f_header('membership operators', membership_operators_demo)
    membership_operators_demo()

    f_header('identity operators', identity_operators_demo)
    identity_operators_demo()

    f_header('operators precedence', operators_precedence_demo)
    operators_precedence_demo()