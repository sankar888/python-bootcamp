'''
    Comprehensions in Python are concise and readable constructs for creating new sequences such as lists, dictionaries, or sets by iterating over iterables. 
    They allow you to perform operations, apply conditions, and construct new data structures in a single line of code.
    Types of comprehension:
    - List
    - Dictionary
    - Set
    - Generator -  Creates a generator object, which produces items lazily (one at a time).
    
    comprehensions can have a optional if statement:
    <expression> for <var> in <iterable> if <condition>
'''
from utils import m_header
from utils import f_header
import random as r

def list_comprehension_demo():
    '''
    List comprehension produces a list by applying a expression on every element of a iterable
    '''
    # string is a interble sequence
    l1 = [x for x in 'sankar']
    print(f'list comprehension: [x for x in "sankar"] =  {l1}')

    # range is a iterable
    l1 = [x**2 for x in range(6)]
    print(f'list comprehension: [x**2 for x in range(6)] =  {l1}')

    # list comprehension with if condition
    l1 = [x**2 for x in range(10) if x % 2 == 0 ]
    print(f'list comprehension: [x**2 for x in range(10) if x % 2 == 0 ] =  {l1}')

    # comprehension expression can be complex expression too
    l1 = [x**2 if x % 2 == 0 else 0 for x in range(10)]
    print(f'list comprehension: [x**2 if x % 2 == 0 else 0 for x in range(10)] =  {l1}')

def dict_comprehension_demo():
    '''
    dict comprehensions creates a dict by specifying the key and value. {} is used for dict comprehension
    '''
    d = {age: 'minor' if age < 18 else 'adult' for age in range(15, 31)}
    print(f'dict cmprehension: age: \'minor\' if age < 18 else \'adult\' for age in r.random(1,100) = {d}')

    d = {k: v for k, v in {1: 'one', 2: 'two'}.items()}
    print(f'dict comprehension: {d}')

    d = {c: ord(c) for c in 'hello'}
    print(f'dict comprehension: c: ord(c) for c in "hello" = {d}')

def set_comprehension_demo():
    '''
    set comprehension creates a set by applying a expression over a iterable. {} is used to create set comprehension
    '''
    s = {x for x in range(1, 11)}
    print(f'set comprehension: {s}')

    # set will have only unique elements
    s = {c for c in 'aabbccdd'}
    print(f'set comprehension: {s}')

def generator_comprehension_demo():
    '''
    generators are objects in python which generate a sequence of values. it doesn't store all the values in memory list list or tuples
    it generates the values on the fly. range functions is an example of generator.
    generators generated using generator comprhension can't be accessed like a sequence like x[2] and its length can't be obtained len(x)
    the value of generators can only be obtained when we are getting the value
    () is used to generate a generator
    '''
    g = (x for x in range(1,6))
    print(f'generator comprehension: {g}')
    print_gen(g)

    g = (x for x in range(6) if x % 2 == 0)
    print_gen(g)

def print_gen(iterable):
    for item in iterable:
        print(f'{item}', end=' ')
    print(' ')

def complex_comprehension_demo():
    '''
    comprehensions can be nested. one comprehension can be used with another.
    it is usually advisable to keep comprehensions simple
    '''
    m = [[y for y in range(1, x)] for x in range(1, 6)]
    print(f'complex comprehension: {m}')

    data = {
        "users": [
            {"name": "Alice", "age": 25, "hobbies": ["reading", "cycling"]},
            {"name": "Bob", "age": 30, "hobbies": ["swimming", "chess"]},
            {"name": "Charlie", "age": 35, "hobbies": ["running", "coding"]}
        ]
    }
    # the following is not nested but chained evaluated from left to right
    hobbies = [hobby for user in data["users"] for hobby in user["hobbies"]]
    print(f"complex comprehensions: {hobbies}")

    # iterating over complex nested structures
    m = ((1, 2), (1,2,3), (1,2,3,4))
    l = [item for tupl in m for item in tupl]
    print(f'complex comprehensions: {l}')

if __name__ == '__main__':
    m_header('Comprehensions in python')
    f_header('List Comprehension', list_comprehension_demo)
    list_comprehension_demo()

    f_header('Dict Comprehension', dict_comprehension_demo)
    dict_comprehension_demo()

    f_header('Set Comprehension', set_comprehension_demo)
    set_comprehension_demo()

    f_header('Generator Comprehension', generator_comprehension_demo)
    generator_comprehension_demo()

    f_header('Complex Comprehension', complex_comprehension_demo)
    complex_comprehension_demo()