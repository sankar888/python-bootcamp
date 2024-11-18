'''
lambdas are annonymous functions which could takes in n no of arguments, but can have only one expreession.
The output of the expression is the output of the function.
lambda function cannot have multiple lines of code since it can have only one expression

lambda function can be assigned to a variable and called like a regular function. but it is discouraged
lambda function is used as input to higher order functions
higher order functions are those which accepts a function as argument
'''
from utils import m_header
from utils import f_header

def lambda_fn_demo():
    # define a simple lambda function
    sqr = lambda x : x * x 
    print(f'lambda demo: sqr(2) = {sqr(2)}, sqr(3) = {sqr(3)}')

    # type of lambda is function
    print(f'type of lambda function is: {type(sqr)}')

    # Used as arguments to functions like map(), filter(), or sorted()
    nums = [1, 2, 3, 4]
    squared = map(lambda x: x ** 2, nums)
    print(f'lambda demo: {list(squared)}')  # Output: [1, 4, 9, 16]

    # sorting with custom keys
    data = [(1, 'a'), (3, 'c'), (2, 'b')]
    sorted_data = sorted(data, key=lambda x: x[1])
    print(sorted_data)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

if __name__ == '__main__':
    m_header('lambda function in python')
    f_header('lambda fn demo', lambda_fn_demo)
    lambda_fn_demo()