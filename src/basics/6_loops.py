'''
loops in python
The main looping structures in Python (for and while), along with loop control statements (break, continue, pass), 
provide flexible options for iterating over data and controlling loop execution.

for - Used to iterate over a sequence (e.g., list, tuple, string, dictionary, range).
while - Executes as long as a specified condition remains True
'''
from utils import m_header
from utils import f_header

def for_loops_demo():
    '''
    for loops iterate over a iterable sequence of objects
    '''
    for i in range(1,10):
        print(f'loop demo: {i}')

    list = [1,2,3]
    for i in list:
        print(f'iterate over list: {i}')

    d = {1: 'one', 2: 'two', 3: 'three'}
    for k, v in d.items():
        print(f'key: {k} , value: {v}')

    for c in "str":
        print(f'looping string: {c}')

def loop_else_demo():
    '''
    for and while loops can have an optional else statement.
    the else statement executes if a loop ends normally and not terminated by break
    or the conditional statement evaluates to false
    '''
    for i in range(1,10):
        pass
    else:
        print(f'for else loop: else loop will be executed because the loop terminates normally')

    for i in range(1,10):
        if i == 3:
            break
    else:
        print(f'for else loop: else loop will not be executed')
    
    # else statement will not be executed if the loop is terminated by break
    i = 1
    while i < 5:
        i += 1
    else:
        print(f'else loop will be executed. because loop terminates normally')

    # else statement will be executed if the while loop evaluates to false
    i = 10
    while i < 5:
        i += 1
    else:
        print(f'else loop will be executed. because loop terminates normally (not even run)')

    i = 1
    while i < 5:
        i += 1
    else:
        print(f'else loop will be executed as the corresponding wile loop terminates normally')


def while_loop_demo():
    '''
    while loops continue to run until the condition evaluates to False
    '''

def break_demo():
    '''
    break will break the inner most loop execution
    '''
    for i in range(1, 25):
       if i == 12:
        num = 12
        break
    print(f'break demo: num is {num}')

def continue_demo():
    '''
    continue statement will skip the current execution of the loop
    '''
    for i in range(1,5): # 5 is exclusive
        if i % 2 == 0:
            continue # continue skips the execution of the statements of the innermost loop encountered after continue 
        print(f'continue demo: {i} is odd')

    for i in range(1,3):
        for j in range(1,5):
            if j % 2 == 0:
                continue
            print(f'odd: {j}') # this will be skipped
        print(f'will not be skipped: {i}')

def pass_demo():
    '''
    pass statements exists as a way to fill up empty function classes or statements
    '''
    def function():
        '''
        not implemented yet
        '''
        pass

if __name__ == '__main__':
    m_header('Loops in Python')
    f_header('For loops', for_loops_demo)
    for_loops_demo()
    
    f_header('for .. else .. loop', loop_else_demo)
    loop_else_demo()

    f_header('break statement', break_demo)
    break_demo()

    f_header('continue statement', continue_demo)
    continue_demo()

    f_header('pass demo', pass_demo)
    pass_demo()