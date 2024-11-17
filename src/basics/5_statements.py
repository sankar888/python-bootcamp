'''
python statements:
    - if
    - if .. else
    - if .. elif 
    - match statement
'''
from utils import m_header
from utils import f_header

def if_statement_demo():
    '''
    if statement conditionally evaluates a block of code
    '''
    if 12:
        print(f'all non zero values are True. zero and empty valus are False')

    if None:
        print('None is false value')

    if "":
        print('empty values are false')

def if_else_statement_demo():
    '''
    if can optionally have a else branch
    '''
    a = -23
    if a >= 0:
        print(f'{a} is positive')
    else:
        print(f'{a} is negative')

def if_else_chain_demo():
    '''
    if statement can have a optional else which might have a if statement
    '''
    a = 27.00
    if a > 50:
        print(f'{a} is over 50%')
    elif a > 30:
        print(f'{a} is over 30%')
    elif a > 10:
        print(f'{a} is over 10%')
    else:
        print(f'{a} less than or equal to 10%')

def ternary_statement_demo():
    '''
    python has a shorthand if else statement which could be used as ternary operator
    '''
    a = 2
    status = "Active" if a > 0 else "Inactive"
    print(f'ternary operator demo: {status}')

def match_statement_demo():
    '''
    In Python 3.10 and later, the match statement was introduced, providing a more flexible and readable way to handle multiple conditional cases. 
    The match statement allows for pattern matching, similar to switch statements in other languages
    '''
    day = 2
    match day:
        case 1: print('monday')
        case 2: print('tuesday')
        case 3: print('wednesday')
        case 4: print('thursday')
        case 5: print('friday')
        case 6: print('saturday')
        case 7: print('sunday')
        case _: print('invalid day') # default case

    l = [1,2,3]
    match len(l):
        case 0: print(f'{l} is empty')
        case _: print(f'{l} is not empty')

    # match can work with complex structures too
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    p = Point(1, 2)
    match p:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"On the y-axis at y={y}")
        case Point(x=x, y=0):
            print(f"On the x-axis at x={x}")
        case Point(x=x, y=y):
            print(f"Point at x={x}, y={y}")

    # multiple case statements
    fruit = "apple"
    match fruit:
        case "apple" | "banana" | "cherry":
            print("It's a common fruit.")
        case "mango":
            print("It's a tropical fruit.")
        case _:
            print("Unknown fruit")

if __name__ == '__main__':
    m_header("Statements in Python")
    f_header('if statement demo', if_statement_demo)
    if_statement_demo()

    f_header('if else statement demo', if_else_statement_demo)
    if_else_statement_demo()

    f_header('if else chain', if_else_chain_demo)
    if_else_chain_demo()

    f_header('ternary operator', ternary_statement_demo)
    ternary_statement_demo()

    f_header('match statement', match_statement_demo)
    match_statement_demo()