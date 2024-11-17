'''
simple_datatypes.py

This module introduces python simple inbuilt datatypes

1. Numeric Types
    int: Integer values, e.g., 10, -5
    float: Floating-point values, e.g., 3.14, -0.001
    complex: Complex numbers, e.g., 3+5j

2. Sequence Types
    str: Immutable text sequence, e.g., "hello"
    list: Mutable ordered sequence, e.g., [1, 2, 3]
    tuple: Immutable ordered sequence, e.g., (1, 2, 3)
    range: Represents a sequence of numbers, often used in loops, e.g., range(5)

3. Mapping Type
    dict: Key-value pairs, e.g., {'a': 1, 'b': 2}

4. Set Types
    set: Unordered collection of unique elements, e.g., {1, 2, 3}
    frozenset: Immutable version of a set, e.g., frozenset([1, 2, 3])

5. Boolean Type
    bool: Represents True or False

6. Binary Types
    bytes: Immutable sequence of bytes, e.g., b'hello'
    bytearray: Mutable sequence of bytes
    memoryview: Provides a memory view of another binary object

7. Special Type
    NoneType: Represents the absence of a value, with the single instance None

In addition to these basic data types, there are some additonal container types which are not covered as part of this module
'''

import utils

def numeric_demo():
    '''
    There are three numeric types in python.
    - int: Integer values, e.g., 10, -5
    - float: Floating-point values, e.g., 3.14, -0.001
    - complex: Complex numbers, e.g., 3+5j
    
    bool is also an implementation of int
    Numeric types are immutable. Operations on numeric type will only lead to a new value
    '''
    # number can be created using numeric literal
    x = 10
    print(f'number can be created from numeric literal {x}')
    x = int(100.23)
    print(f'number can be created from casting other numeric values int({x}) = {int(x)}')

    # what will happen if we cast non numeric types. we couldn't do it.
    # A ype error will be thrown
    l = [1,2,3]
    print(f'int({l}) will throw TypeError')

    # numeric types are immutable.
    x = 100
    print(f'x = 100, id({x}) is {id(x)}')
    x += 1
    print(f'after x += 1, id({x}) is {id(x)}, which is different from above id')


def sequence_type_demo():
    '''
    Python sequence type are collections of objects. the collections could be of same type or different type. Common sequence types are
    
    - str: Immutable text sequence, e.g., "hello"
    - list: Mutable ordered sequence, e.g., [1, 2, 3]
    - tuple: Immutable ordered sequence, e.g., (1, 2, 3)
    - range: Represents a sequence of numbers, often used in loops, e.g., range(5)

    In Python, the common base class for all sequence types (like list, tuple, and str) is collections.abc.Sequence, an abstract base class in the collections module.
    Common Methods and Properties in collections.abc.Sequence
    
    Indexing and Slicing:
    __getitem__(index): Allows element access using square brackets, e.g., seq[index].
    Slicing Support: Sequences can be sliced, e.g., seq[start:end:step].
    
    Length and Membership:
    __len__(): Returns the length of the sequence with len(seq).
    __contains__(item): Checks membership with in, e.g., item in seq.
    
    Iteration:
    __iter__(): Allows iteration over the sequence in a for-loop, e.g., for item in seq.
    
    Concatenation and Repetition:
    __add__(other): Supports concatenation using +, e.g., seq1 + seq2.
    __mul__(count): Allows repetition using *, e.g., seq * n.
    
    Index and Count:
    index(value, [start, [stop]]): Returns the index of the first occurrence of a value.
    count(value): Returns the number of occurrences of a value in the sequence.

    There are also membership operators 'in' and 'not in' which check for membership in any collection
    '''
    
    # all basic sequences str, list, tuple, range can be created via a literal or through a function
    # str - ordered immutable collection of strings
    s = "helloworld"
    s1 = str(123)
    
    # list - ordered mutable collection. can be hetrogeneous
    l = [1,2,3]
    l1 = list(range(1,5))

    # tuple - ordered immutable collection. can be hetrogeneous
    t = (1,2,3)
    t1 = tuple(range(1,5))

    # range - doesn't store all values. but behaves like a collection. usually use din for loops. immutable collection
    r = range(1,10,2) # rane doesn't have literal representation

    # all basic sequence can be accessed by index and slices can be created
    # str
    print(f's = {s}, s[0] is {s[0]}, s[len(s) - 1] is {s[len(s) - 1]}')
    print(f't = {t}, t[0] is {t[0]}')
    print(f'l = {l1}, l1[1] = {l1[1]}')
    print(f'r = {r}, r[1] = {r[1]}')

    # str, tuple and range are immutable. only list is mutable
    print(f't = {t}, Assigning, t[0] = -1 will result in TypeError')
    print(f'l1 = {l1}, Assigning l1[0] = -100 will chane the list')
    l1[0] = -100
    print(f'l1 = {l1}')
    print('l1 = {l1}, assigning values to out of box index like l1[6] = -100 will cause IndexError')

    # slice - data can be sliced form any sequence using seq[start:end:step]
    # default values for start = 0, end = len(seq), step = 1
    # start, end, step can be positive or negative
    # if no slice can be sliced. empty seq is returned. slice always returns a copy of original seq
    l = list(range(1,30))
    print(f'l = {l}, l[:] will return a new list. id(l) is {id(l)}, id(l[:]) is {id(l[:])}')
    print(f'l[10:0:-2] is {l[10:0:-2]}')
    print(f'l[0:10:-2] is {l[0:10:-2]}. empty sequence')

    # add items to sequence. 
    l = [1,2,3]
    l.append(4)
    print(f'appended list {l}')

    # delete a sequence member
    # only mutable sequence can be deleted. it could be deleted by assigining a empty seq or using del keyword
    l = list(range(1, 11))
    print(f'l = {l}. assigning l[3:10] = [] will delete the sequence members from 3 to 9 index')
    l[3:10] = []
    print(f'l = {l}')
    
    # del keyword can also used to delete a slice of data
    del l[2]
    print(f'after deleting l[2], l = {l}')

def map_type_demo():
    '''
    dict is the map type in python. it can have heterogeneous keys and values.
    The key shuld be immutable and hashable. ex string, number , tuple, etc..
    dict values are accessed by keys.
    dict is mutable. del keywork can be used to delete a key

    Dictionaries can be created by several means:
    Use a comma-separated list of key: value pairs within braces: {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}
    Use a dict comprehension: {}, {x: x ** 2 for x in range(10)}
    Use the type constructor: dict(), dict([('foo', 100), ('bar', 200)]), dict(foo=100, bar=200)
    '''
    # create a dict
    d = {1: 'one', 2: 'two', 'three': 3}
    d1 = dict() # empty
    print(f'creating dict: d is {d} , d1 is {d1}')

    # accessing dict
    print(f'accessing dict: d[2] is {d[2]}')
    print(f'accessing dict using get: d.get(2, default=0) is {d.get(2, 0)}')

    # todo: deleting dict and merging etc..

def set_type_demo():
    pass

def bool_type_demo():
    pass

def binary_type_demo():
    pass

def none_type_demo():
    pass

if __name__ == '__main__':
    utils.m_header('Python\'s Built-in Data Types')
    utils.f_header('numeric type', numeric_demo)
    numeric_demo()

    utils.f_header('sequence data type', sequence_type_demo)
    sequence_type_demo()

    utils.f_header('dict data type', map_type_demo)
    map_type_demo()

# todo: complete the simple datatypes